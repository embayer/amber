#####################################################
# Dockerfile to build the kumpel queue application. #
# Based on Ubuntu 14.04 LTS Trusty Tahr             #
#####################################################

# set the base image
FROM ubuntu:14.04

# file Author
MAINTAINER Markus Bayer

# update the sources list & install basic applications
RUN apt-get update && apt-get install -y tar \
                   build-essential \
                   libncurses5-dev \
                   libxml2-dev \
                   libxslt1-dev \
                   zlib1g-dev \
                   libreadline6 \
                   libreadline6-dev

# install Python and basic Python tools
RUN apt-get install -y python \
                    python-dev \
                    python-distribute \
                    python-pip

# copy the application folder inside the container
ADD . /amber-cloud

# get pip to download and install requirements:
RUN pip install -r /amber-cloud/requirements.txt

# expose ports
EXPOSE 80

# set the default directory where CMD will execute
WORKDIR /amber-cloud/bin

# create and use a non root user
# RUN groupadd -r celery && useradd -r -g celery celery
# USER celery

# set the default command to execute when creating a new container
CMD ["bash", "./celery"]
