# Download base image
FROM alpine:3.8

LABEL AUTHOR="Quinn D Granfor, spootdev@gmail.com"
LABEL Description="This image holds the base image"

ARG ALPMIRROR
ARG PIPMIRROR

# create work dir
RUN mkdir /librepacs

WORKDIR /librepacs

# pip3 is installed with python3
RUN sed -i "s/dl-cdn.alpinelinux.org/${ALPMIRROR}/" /etc/apk/repositories \
  && apk add --update \
  python3 \
  # still installing and upgrading pip since other images will use it
  && pip3 install --trusted-host ${PIPMIRROR} -i https://${PIPMIRROR}/simple --upgrade pip \
  && rm -rf /var/cache/apk/*

CMD ["/bin/ash"]
