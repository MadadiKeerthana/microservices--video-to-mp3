#each line is a layer and layers can be cached if there are no changes for a particular layer between builds

#builds on top of a base python image, base image is a screenshot of a file system with all dependencies for python 
FROM python:3.10-slim-bullseye

#installing os dependencies, flags avoid neccessary installs and caching to make the container as light as possible
RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential default-libmysqlclient-dev pkg-config \
    && pip install --no-cache-dir --upgrade pip

WORKDIR /app
#requirements are separate and before the other code changes
COPY ./requirements.txt /app
#separate requirements make sure that this is layer is isolated as it is the most time consuming
RUN pip install --no-cache-dir --requirement /app/requirements.txt

#if there is a change in code, all layers need to be rebuilt starting from this layer
COPY . /app

#commands are split
CMD ["python3", "consumer.py"]
