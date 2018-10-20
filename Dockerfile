FROM python:3.6.5-slim

RUN apt-get -qq -y update

RUN export PYTHONIOENCODING=utf-8

workdir /app
COPY . /app

RUN pip install -r requirements/common.txt

ENTRYPOINT ["python", "app.py"]
