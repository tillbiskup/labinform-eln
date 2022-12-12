=======================
Developer documentation
=======================

Welcome to the developer documentation of the LabInform ELN. This part gives some general background information for developers who want to actively contribute to the project.


Code organisation
=================

Currently, the repository contains two parts: the DokuWiki contents of a demo installation of the LabInform ELN, and the documentation. The former can be run and developed locally using a Docker container. An abbrevated directory listing is provided below as a first overview:

.. code-block::

    .
    ├── docs
    │   ├── ...
    └── dokuwiki
        ├── conf
        ├── data
        │   ├── media
        │   ├── meta
        │   └── pages
        └── Dockerfile


As obvious, the documentation (*i.e.* what you are actually reading) resides in the ``docs`` directory, while the DokuWiki contents for the LabInform ELN together with the Dockerfile for local development reside in the ``dokuwiki`` directory.

Later, there may be more directories, *e.g.* in case of a Python module/package for interacting with the LabInform ELN via XML-RPC interface. For ideas see the :doc:`roadmap`.


Documentation
=============

(This) Documentation is available online (`https://eln.docs.labinform.de <https://eln.docs.labinform.de>`_) and created using `Sphinx <https://www.sphinx-doc.org/>`_. Locally, it resides in the ``docs`` directory. To create the documentation locally, you need to have a working Python installation with a few packages. As always with Python projects, it is highly recommended to create a virtual environment and install the required packages locally there. Assuming a working Python installation and a unixoid operating system, the necessary steps are as follows:

.. code-block:: bash

    # Create virtual environment
    python3 -m venv labinform-eln-documentation

    # Activate virtual environment
    source labinform-eln-documentation/bin/activate

    # Install required packages
    pip install sphinx sphinx-rtd-theme


To create the actual documentation locally, ensure to have the virtual environment active, change into the documentation directory (``docs``) and create the documentation. Again, a unixoid operating system is assumed:

.. code-block:: bash

    # Change to documentation directory
    cd docs

    # Create documentation locally
    make html


To view the just built documentation, point your browser to the correct directory, as shown in the last output line of Sphinx (usually the subdirectory ``_build/html``).


Docker container
================

To ease development of the LabInform ELN, a Docker container is provided that can be run locally. The same docker container will eventually run the demo instance available online at `<https://eln.labinform.de/>`_.

To start the Docker container, change to the ``dokuwiki`` directory and run the following command, assuming you have a working Docker installation and had built the container previously:

.. code-block:: bash

    docker run --name eln -d -p 8081:8080 \
        -v "`pwd`/data/pages:/srv/www/data/pages" \
        -v "`pwd`/data/media:/srv/www/data/media" tillbiskup/labinform-eln

This will start the Docker container, name it ``eln``, mount a few local directories and bind the HTTP port of the container to the local port ``8081``. To view your LabInform ELN, direct your browser to the address `<http://localhost:8081/>`_.

If the container won't start and you get a message instead that the name is used already, this usually means that either a container with the same name exists already or that you had it rnu previously. In this case, simply delete the old container:

.. code-block:: bash

    docker rm eln

If you didn't build the container already, obviously you need to do this before you can run it:

.. code-block:: bash

    docker build . -t 'tillbiskup/labinform-eln'

