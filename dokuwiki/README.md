# Developer documentation: docker

The `Dockerfile` is used to create a docker image for test purposes. This file requires a series of docker containers to be available, namely `tillbiskup/nginx`, `tillbiskup/nginx-php`, `tillbiskup/dokuwiki`, and `tillbiskup/dokuwiki-eln`.

Note that there is now an additional docker file called `Dockerfile-standalone` that does not depend on the series of other containers and that can used for local deployment and testing purposes. To explicitly use this docker file, add `-f Dockerfile-standalone` to the `docker build` command below and/or change your `docker-compose.yml` file accordingly.

However, please note that none of these docker containers are yet in a state that they should be used for deploying production-ready containers. At least, in a production environment, you would like to have a backup strategy in place.


## Using docker

There are two ways of working with the Dockerfile: using plain docker, and using docker compose. Here, the first option is described. For how to use docker compose, see below.

### Build image

To build the image:

    docker build . -t 'tillbiskup/labinform-eln'

### Run the container

To run the container:

    docker run --name eln -d -p 8081:8080 -v "`pwd`/data/pages:/srv/www/data/pages" -v "`pwd`/data/media:/srv/www/data/media" tillbiskup/labinform-eln

This will add the name `eln` to the running container and bind-mount the local directories `data/pages` and `data/media` accordingly.

**Important:** The above command needs to be issued from within the `dokuwiki` directory or otherwise the paths for the volumes need to be adapted. Otherwise, your wiki will not work properly (not finding any content and complaining right away).

To see the running LabInform ELN instance, navigate with your browser to [localhost:8081/](http://localhost:8081/)

Currently, the credentials are demo-admin:eln-admin and demo-user:eln-user

### Stop and remove the container

To stop and remove the container:

    docker stop eln; docker rm eln


## Using docker compose

There are two ways of working with the Dockerfile: using plain docker, and using docker compose. Here, the second option is described. For how to use plain docker, see above.

### Run the container

Usually, running the container is as simple as:

    docker compose up -d

Here, ``-d`` implies running as demon.

Note that there is no need to build the image beforehand, as that is been taken care of automatically by docker compose. However, if you need to rebuild the image, see below.

### (Re)build the image

As mentioned above, initially building the image before running the container is not necessary, as docker compose takes care of that for you. However, to rebuild the container (particularly important for testing), run this commmand:

    docker compose build

### Stop (and remove) the container

To just stop the container, run this command:

    docker compose down

To remove the container as well, run the following command:

    docker compose rm

