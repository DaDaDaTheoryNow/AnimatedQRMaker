FROM python:3.8

RUN mkdir /AnimatedQRMaker

WORKDIR /AnimatedQRMaker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /src

CMD uvicorn main:app --host 0.0.0.0 --port 80