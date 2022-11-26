FROM tillbiskup/dokuwiki-eln

ENV UID=1000

USER root

# Copy local data
COPY data/media/* /srv/www/data/media/
COPY data/meta/* /srv/www/data/meta/
COPY conf/* /srv/www/conf/
RUN mkdir -p /srv/www/conf/lang/en/
COPY conf/lang/en/* /srv/www/conf/lang/en/

RUN usermod -u ${UID} nobody && echo ${UID}

RUN chown -R nobody.nobody /srv/www

# Make config read-only (demo container, to not allow changing settings)
RUN chmod ugo-w /srv/www/conf/

USER nobody

