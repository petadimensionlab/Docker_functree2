FROM alpine:3.10
MAINTAINER petadimensionlab

RUN apk --update add --no-cache \
    python3 \
    python3-dev \
    nano \
    curl \
&& pip3 install --upgrade pip 

ADD functree2_docker.py /tmp

WORKDIR /tmp