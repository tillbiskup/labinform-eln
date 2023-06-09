.. image:: images/zenodo.xxxxxxx.svg
   :target: https://doi.org/10.5281/zenodo.#######
   :align: right

===========================
LabInform ELN documentation
===========================


Welcome! This is the documentation for the LabInform ELN component, the **electronic laboratory notebook (ELN)** that is part of the `LabInform laboratory information and management system <https://www.labinform.de/>`_ (LIMS).

Why yet another open-source ELN? Aren't there enough already? We are pretty certain that the LabInform ELN comes with some :ref:`unique features <sec-features>`, and we look back at already ten years of successful operation. However, rather than telling you into using the LabInform ELN, we explain the :doc:`underlying design principles <concepts>` and highlight the decisions necessary to achieve a workflow fitting the local requirements and improving reproducibility and hence overall quality of science, besides helping with getting FAIRer data.

.. important::
    A **demo of the LabInform ELN** can be accessed online: `<https://eln.labinform.de/>`_.

    The data contained in this demo will be deleted regularly. Nevertheless, don't enter any sensible data in there, as everybody will be able to access them.

    For more information on how to use the LabInform ELN from a user perspective, have a look at the :doc:`user manual <user/index>`.



.. _sec-features:

Features
========

*A number of good reasons why to choose the LabInform ELN instead of other ELN candidates.*


System:

* Based on `DokuWiki <https://www.dokuwiki.org/>`_, "a simple to use and highly versatile Open Source wiki software".\ [#fn1]_
* Small footprint: minimum system requirements, simple installation, *no database backend*
* Flexible, easily adapted to your needs from *within* the Web UI
* Fine-grained access control and role model
* Hierarchical structure, well-suited for knowledge management
* Easy to backup: just a folder in the file system
* Complete audit trail of changes


Contents:

* Flexible contents including media, thanks to simple yet powerful DokuWiki markup syntax
* Structured content, machine-actionable with little to no effort
* Inventory for samples
* Automatic cross-linking between inventory and labbook entries
* new entries via web forms and configurable templates


And to make it even more convenient for users and future-proof:

* Open source project
* Extensive documentation for :doc:`users <user/index>`, :doc:`administrators <admin/index>`, and :doc:`developers <developer/index>`
* Large and vivid `DokuWiki <https://www.dokuwiki.org/>`_ user community
* `DokuWiki <https://www.dokuwiki.org/>`_ itself written in PHP, focussing on high code quality


Non-Features
============

A few things the LabInform ELN does *not* provide/implement by purpose:

* Data store, aka repository\*
* Research data catalogue
* Management of measurement setups in the lab\*
* General project management, including proposals and publications\*
* General inventory for consumables
* Analysis workflow for data\*\*

The main reason lies in the "separation of concerns" (E. Dijkstra), focussing on one task at a time using one dedicated tool. Some of the "non-features" described above (and marked with an asterisk: \*) are, however, part of the `wider LabInform LIMS <https://www.labinform.de/>`_ the LabInform ELN is only one part of. If you are interested in a reproducible analysis workflow of spectroscopic data (\*\*), have a look at the `ASpecD framework <https://docs.aspecd.de/>`_ and related packages.


.. _sec-how_to_cite:

How to cite
===========

The LabInform ELN is free software. However, if you use the LabInform ELN as crucial infrastructure component of your own research, please cite both, the article describing it and the software itself:

* Mirjam Schröder, Till Biskup. LabInform ELN: A lightweight and flexible electronic laboratory notebook for academic research based on the open-source software DokuWiki. *ChemRxiv*, 2023. doi:`10.26434/chemrxiv-2023-2tvct <https://doi.org/10.26434/chemrxiv-2023-2tvct>`_

* Mirjam Schröder, Till Biskup. Labinform ELN (2023). doi:10.5281/zenodo.#######

To make things easier, the LabInform ELN has a `DOI <https://doi.org/10.5281/zenodo.#######>`_ provided by `Zenodo <https://zenodo.org/>`_, and you may click on the badge below to directly access the record associated with it. Note that this DOI refers to the software as such and always forwards to the most current version.

.. image:: images/zenodo.xxxxxxx.svg
   :target: https://doi.org/10.5281/zenodo.#######




Where to start
==============

If you want to know what it is all about or are unsure whether the LabInform ELN is interesting for you, start :doc:`right at the beginning <audience>`. If you are a user of the LabInform ELN and look for how to do things, the :doc:`user manual <user/index>` should be the right place. If you want to install the LabInform ELN or are the person with IT competence in charge of keeping it running, have a look at the :doc:`administrator manual <admin/index>`. Finally, if you are interested in contributing to the LabInform ELN, the :doc:`developers corner <developer/index>` is the right place for you.



Installation
============

Generally, DokuWiki requires a running web server and PHP, but no database. Hence, basic familiarity with setting up a web server and with the command line are necessary. The LabInform ELN builds upon a series of plugins for DokuWiki. Detailed installation instructions can be found in the :doc:`administrator manual <admin/index>`.



Related projects
================

There is a number of related packages users of the LabInform ELN may well be interested in, as they have a similar scope, focussing on spectroscopy and reproducible research.

* `ASpecD <https://docs.aspecd.de/>`_

  A Python framework for the analysis of spectroscopic data focussing on reproducibility and good scientific practice.



.. toctree::
   :maxdepth: 2
   :caption: Overview:
   :hidden:

   audience
   introduction
   concepts
   usecases
   adapting


.. toctree::
   :maxdepth: 2
   :caption: User Manual:
   :hidden:

   user/index
   user/workflow
   user/batches
   user/samples
   user/measurements
   user/molecules
   user/geometries
   user/calculations


.. toctree::
   :maxdepth: 2
   :caption: Administrator Manual:
   :hidden:

   admin/index
   admin/installing
   admin/organisation
   admin/forms_templates


.. toctree::
   :maxdepth: 2
   :caption: Developers Corner:
   :hidden:

   developer/index
   developer/people
   developer/developers
   developer/changelog
   developer/roadmap


License
=======

This program is free software: you can redistribute it and/or modify it under the terms of the **BSD License**. However, if you use the LabInform ELN as crucial infrastructure component of your own research, please cite it appropriately. See :ref:`How to cite <sec-how_to_cite>` for details.

Please note that DokuWiki itself is provided under a GNU General Public License (GPL). For details, see `their webpage <https://www.dokuwiki.org/faq%3Alicense>`_. Most DokuWiki plugins are licensed under the GNU GPL as well, but please check yourself for each plugin you're using.


A note on the logo
==================

The "L" of the LabInform logo originates from the Computer Modern Roman font originally designed by Donald E. Knuth for his TeX typesetting system. As such, it represents science and the scientific method. Harbouring the "i" representing the information bit puts things right: Proper and reproducible science is the solid support for all the information we can retrieve. The copyright of the LabInform logo belongs to J. Popp. The added symbol on the bottom right is taken from FontAwesome.


.. rubric:: Footnotes

.. [#fn1] "DokuWiki is a simple to use and highly versatile Open Source wiki software that doesn't require a database. It is loved by users for its clean and readable syntax. The ease of maintenance, backup and integration makes it an administrator's favorite. Built in access controls and authentication connectors make DokuWiki especially useful in the enterprise context and the large number of plugins contributed by its vibrant community allow for a broad range of use cases beyond a traditional wiki." source: https://www.dokuwiki.org/ (accessed 2023-02-22)