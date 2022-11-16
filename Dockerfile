FROM python:3.9-bullseye

ENV DEBIAN_FRONTEND="noninteractive"

RUN apt-get update && apt-get install libsm6 libxext6 build-essential git -y

ADD requirements.txt .
RUN pip install -r requirements.txt

RUN useradd -ms /bin/bash graphs_from_scratch
USER graphs_from_scratch

WORKDIR /home/graphs_from_scratch/workspace
ENV PYTHONPATH '${PYTHONPATH}:/home/graphs_from_scratch/workspace'
