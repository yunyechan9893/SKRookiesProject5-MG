FROM python:3.11.3 AS builder
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx

COPY . /long_memory/
WORKDIR /long_memory

RUN pip install -r requirements.txt

ENV FLASK_APP run.py
ENV FLASK_DEBUG True
ENV FLASK_RUN_PORT 3333
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 3333
 
WORKDIR /long_memory

CMD ["flask", "run"]
