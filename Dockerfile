# syntax=docker/dockerfile:1

FROM python:3.10.12

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . .
EXPOSE 8000
CMD [ "gunicorn", "app:app", "--bind", "0.0.0.0:8000"]