FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim
WORKDIR /app

RUN pip install fastapi

EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
