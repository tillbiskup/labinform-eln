# Developer documentation: docker

The `Dockerfile` is used to create a docker image for test purposes. This file requires a series of docker containers to be available, namely `tillbiskup/nginx`, `tillbiskup/nginx-php`, `tillbiskup/dokuwiki`, and
`tillbiskup/dokuwiki-eln`.

## Build image

To build the image:

    docker build . -t 'tillbiskup/labinform-eln'

## Run the container

To run the container:

    docker run --name eln -d -p 8081:8080 -v "`pwd`/data/pages:/srv/www/data/pages" -v "`pwd`/data/media:/srv/www/data/media" tillbiskup/labinform-eln

This will add the name `eln` to the running container and bind-mount the local directories `data/pages` and `data/media` accordingly.

To see the running LabInform ELN instance, navigate with your browser to [localhost:8081/](localhost:8081/)

Currently, the credentials are super:admin


## Stop and remove the container

To stop and remove the container:

    docker stop eln; docker rm eln
