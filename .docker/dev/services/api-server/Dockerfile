############################################################
# Dockerfile to build the Kannji API server image for local development
############################################################
FROM python:3.6.3-alpine3.6
LABEL maintainer = "Jan-Luca Klees"

# Make everything fresh
RUN apk update && apk upgrade

# pip
RUN pip install 'hug==2.3.2'

# copy entrance point
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

# image config
WORKDIR /kannji/api-server/
EXPOSE 80