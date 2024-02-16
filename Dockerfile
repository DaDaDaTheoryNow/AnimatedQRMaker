FROM python:3.12
COPY requirements.txt /app/requirements.txt
WORKDIR /app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]