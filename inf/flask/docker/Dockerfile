FROM alpine:latest
RUN apk add --no-cache python3 python3-dev py3-pip postgresql alpine-sdk \
    && python -m venv /srv/flask \
    && /srv/flask/bin/pip install -U pip pipenv
COPY Pipfile /srv/flask/Pipfile
COPY Pipfile.lock /srv/flask/Pipfile.lock
WORKDIR /srv/flask
RUN /srv/flask/bin/pipenv requirements > requirements \
    && /srv/flask/bin/pip install -r requirements
RUN /srv/flask/bin/pip install flask-sqlalchemy
