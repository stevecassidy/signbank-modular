# pull official base image
FROM python:3.8.3-alpine

## install build dependencies
RUN apk add build-base libffi-dev openssl-dev postgresql-dev git ffmpeg

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt .
ADD ./requirements-deploy.txt .
RUN echo 'hello there'
RUN pip install -r requirements.txt
RUN pip install -r requirements-deploy.txt
 
# copy project
COPY . .

ENV STATIC_ROOT=/usr/src/app/signbank/staticfiles

RUN python bin/production.py collectstatic --no-input -v 2


