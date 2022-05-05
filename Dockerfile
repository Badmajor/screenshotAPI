FROM python:3.9-alpine as spi4ka
RUN apk update
RUN apk add gcc python3-dev libc-dev libffi-dev
COPY . /screenshotAPI
WORKDIR /screenshotAPI
RUN pip install -r requirements.txt
CMD python main.py