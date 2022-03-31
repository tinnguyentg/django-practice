FROM python:3.9.6-alpine as BUILDER

WORKDIR /usr/src/app

COPY ./requirements ./requirements
RUN pip install -r ./requirements/prod.txt