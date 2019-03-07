FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /app/api
ADD requirements.txt /app/api/
RUN apt-get update
RUN pip install -r requirements.txt
ADD . /app/api/

