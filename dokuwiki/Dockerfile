FROM tillbiskup/dokuwiki-eln

ENV UID=1000

USER root

# Copy local data
COPY data/media/* /srv/www/data/media/
COPY data/meta/* /srv/www/data/meta/
COPY conf/* /srv/www/conf/

RUN usermod -u ${UID} nobody && echo ${UID}

RUN chown -R nobody.nobody /srv/www

USER nobody

