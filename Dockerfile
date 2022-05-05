FROM python:3.9-alpine as spi4ka
RUN apk update
RUN apk add gcc python3-dev libc-dev libffi-dev firefox
RUN mkdir /req
COPY requirements.txt /req
RUN pip install -r /req/requirements.txt