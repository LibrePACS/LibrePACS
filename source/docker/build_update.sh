git pull
./source_sync.sh

docker-compose down

# base python 3 images
cd ./Alpine38Py3
docker build -t librepacs/lbalpine38py3 --build-arg ALPMIRROR=10.0.0.122 --build-arg PIPMIRROR=pypi.python.org .

# move here so all the "deps" are built first
docker-compose build

# containers here and later are "standalone" with no deps

# retag all the images - need to back out of docker/alpine as well as docker directory for container
./tag_rename_images.sh
