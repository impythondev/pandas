FROM python:3.6-alpine

RUN apk update && pip install -U pip

RUN apk add build-base


WORKDIR /app

COPY . /app


RUN pip install -r requirement.txt

