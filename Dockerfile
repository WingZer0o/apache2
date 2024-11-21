FROM nvidia/cuda:11.8.0-base-ubuntu22.04

RUN apt-get update && \
       apt-get install -y python3 python3-pip

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000
CMD [ "gunicorn", "-c", "gunicorn.conf.py", "app:app"]