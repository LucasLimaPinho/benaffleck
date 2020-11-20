FROM python:alpine3.6
RUN pip install -r requirements.txt
RUN mkdir /app
WORKDIR /app
ADD . /app/

