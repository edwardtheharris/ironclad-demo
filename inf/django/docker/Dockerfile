FROM alpine:latest
RUN apk add --no-cache python3 python3-dev py3-pip postgresql alpine-sdk \
    && python -m venv /srv/django \
    && /srv/django/bin/pip install -U pip pipenv
COPY Pipfile /srv/django/Pipfile
COPY Pipfile.lock /srv/django/Pipfile.lock
WORKDIR /srv/django
RUN /srv/django/bin/pipenv requirements > requirements \
    && /srv/django/bin/pip install -r requirements
