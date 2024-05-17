FROM python:3.12.3-alpine

WORKDIR /flaskUploader

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

#install system dependecies
#RUN apk update \
#     && apk add gcc python3-dev musl-dev

COPY ./requirements.txt /flaskUploader

RUN pip install -r requirements.txt

COPY . .


