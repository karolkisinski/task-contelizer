FROM python:3.11-slim

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /api
COPY ./ /api/

RUN pip install -r requirements.txt

EXPOSE 8000
