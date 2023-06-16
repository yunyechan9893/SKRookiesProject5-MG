FROM python:3.11.3 AS builder
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx

COPY . /backend/
WORKDIR /backend

RUN pip install -r requirements.txt

ENV FLASK_APP backend.py
ENV FLASK_DEBUG True
ENV FLASK_RUN_PORT 8000
ENV FLASK_RUN_HOST 0.0.0.0


EXPOSE 8000
 
WORKDIR /backend

CMD ["flask", "run"]


