FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim
WORKDIR /app

RUN pip install fastapi uvicorn celery redis flower pydantic

COPY . .

EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
