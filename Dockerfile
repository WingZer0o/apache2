FROM nvidia/cuda:11.8.0-base-ubuntu22.04 as build

RUN apt-get update && \
       apt-get install -y python3 python3-pip

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000

FROM build as dev
RUN pip install debugpy
CMD ["python3", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", "flask", "run", "--port", "8000", "--host=0.0.0.0"]

FROM build as prod
CMD [ "gunicorn", "-c", "gunicorn.conf.py", "app:app"]