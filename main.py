from typing import Optional, Any
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def get_data():
    response = {
        'ok': 'Hello World!'
    }
    return response
