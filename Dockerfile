FROM python:3.9-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev

RUN mkdir /app

WORKDIR /app

ADD . /app/

EXPOSE 8000

RUN python -m pip install --upgrade pip --default-timeout=100 future

RUN pip install -r requirements.txt
