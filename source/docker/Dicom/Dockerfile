# Download base image
FROM librepacs/lbalpine38py3

LABEL AUTHOR="Quinn D Granfor, spootdev@gmail.com"
LABEL Description="This image holds the dicom app"

ARG ALPMIRROR
ARG PIPMIRROR

# copy PIP requirements
ADD requirements.txt /librepacs
WORKDIR /librepacs

RUN sed -i "s/dl-cdn.alpinelinux.org/${ALPMIRROR}/" /etc/apk/repositories \
  && apk add --update \
  alpine-sdk \
  py3-psycopg2 \
  && pip3 install --trusted-host ${PIPMIRROR} -i https://${PIPMIRROR}/simple -r requirements.txt \
  && rm -rf /var/cache/apk/* \
  && rm requirements.txt

ADD wait-for-it-ash.sh /librepacs
# Copy the source files for the app
ADD src /librepacs

CMD ["/bin/ash"]
