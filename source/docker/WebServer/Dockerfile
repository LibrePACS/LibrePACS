# Download base image
FROM librepacs/lbalpine38py3

LABEL AUTHOR="Quinn D Granfor, spootdev@gmail.com"
LABEL Description="This image holds the image for the web server app"

ARG ALPMIRROR
ARG PIPMIRROR

# copy PIP requirements
ADD requirements.txt /librepacs
WORKDIR /librepacs

# Update repository and install packages
RUN sed -i "s/dl-cdn.alpinelinux.org/${ALPMIRROR}/" /etc/apk/repositories \
  && apk add --update \
  ack \
  curl-dev \
  git \
  gcc \
  jpeg-dev \
  libffi-dev \
  libxml2-dev \
  libxslt-dev \
  linux-headers \
  musl-dev \  
  openrc \
  libressl-dev \
  py3-cffi \
  py3-redis \
  python3-dev \
  ca-certificates \
  libressl \
  py3-numpy \
  py3-psycopg2 \
  py3-psutil \
  && export PYCURL_SSL_LIBRARY=openssl \
  && pip3 install --trusted-host ${PIPMIRROR} -i https://${PIPMIRROR}/simple pycurl \
  && pip3 install --trusted-host ${PIPMIRROR} -i https://${PIPMIRROR}/simple -r requirements.txt \
  && pip3 install git+https://github.com/MediaKraken/flask-pika \
  && apk del \
  gcc \
  git \
  musl-dev \
  linux-headers \
  python3-dev \
  libressl-dev \
  && rm requirements.txt \
  && apk add \
  uwsgi-python3 \
  uwsgi-router_uwsgi \
  py-setuptools \
  && cp /usr/lib/uwsgi/python3_plugin.so /librepacs/. \
  && rm -rf /var/cache/apk/* \
  && rc-update add netmount \
  && rc-update add rpcbind

ADD wait-for-it-ash.sh /librepacs
# Copy the source files for the app
ADD src /librepacs

EXPOSE 8080
CMD ["/bin/ash"]
