FROM alpine:latest
RUN apk add --no-cache python3 python3-dev py3-pip \
    && pip install -U pip pipenv \
    && mkdir -pv /srv/django
COPY Pipfile /srv/django
COPY Pipfile.lock /srv/django
WORKDIR /srv/django
RUN pipenv install --deploy --ignore-pipfile
