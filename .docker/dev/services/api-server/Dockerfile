############################################################
# Dockerfile to build the Kannji API server image for local development
############################################################
FROM python:3.6.3-alpine3.6
LABEL maintainer = "Jan-Luca Klees"

# Make everything fresh
# build-deps, gcc, python3-dev, musl-dev and postgresql-dev are needed for building and installing psycopg2
RUN apk update && apk upgrade && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev

# pip
RUN pip install 'hug==2.3.2' 'psycopg2==2.7.3.2' 'peewee==2.10.2' uuid

# copy entrance point
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

# image config
WORKDIR /kannji/api-server/
EXPOSE 80