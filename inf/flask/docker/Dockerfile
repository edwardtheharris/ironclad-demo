FROM alpine:latest
RUN apk add --no-cache python3 python3-dev py3-pip \
    && python -m venv /srv/flask \
    && /srv/flask/bin/pip install -U pip pipenv
COPY Pipfile /srv/flask/Pipfile
COPY Pipfile.lock /srv/flask/Pipfile.lock
WORKDIR /srv/flask
RUN pipenv requirements > requirements \
    && /srv/flask/bin/pip install -r requirements
