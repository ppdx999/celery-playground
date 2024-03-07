from typing import Optional, Any
from fastapi import FastAPI
from pydantic import BaseModel
from tasks import celery, calc_sum

app = FastAPI()

@app.get('/')
async def get_data():
    response = {
        'ok': 'Hello World!'
    }
    return response

class Sum(BaseModel):
    x: float
    y: float


class TaskStatus(BaseModel):
    id: str
    status: Optional[str]
    result: Optional[Any]


@app.post('/sum', response_model=TaskStatus, response_model_exclude_unset=True)
def calculate_sum(sum: Sum):
    task = calc_sum.delay(x=sum.x, y=sum.y)
    return TaskStatus(id=task.id)


@app.get('/sum/{task_id}', response_model=TaskStatus)
def check_status(task_id: str):
    result = celery.AsyncResult(task_id)
    status = TaskStatus(id=task_id, status=result.status, result=result.result)
    return status
