FROM python:3.8-alpine
MAINTAINER Dozero Bus Time App Developer

ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN python -m pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN adduser -D user
USER user