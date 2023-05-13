# LabInform ELN

This is the LabInform ELN component, the electronic lab(oratory) notebook (ELN) that is part of the [LabInform laboratory information and management system](https://www.labinform.de/) (LIMS).

Why yet another open-source ELN? Aren't there enough already? We are pretty certain that the LabInform ELN comes with some unique features, and we look back at already ten years of successful operation. However, rather than telling you into using the LabInform ELN, in the [documentation available online](https://eln.docs.labinform.de/) we explain the underlying design principles and highlight the decisions necessary to achieve a workflow fitting the local requirements and improving reproducibility and hence overall quality of science, besides helping with getting FAIRer data.


## Demo available online

A **demo of the LabInform ELN** can be accessed online: https://eln.labinform.de/.

The data contained in this demo will be deleted regularly. Nevertheless, don't enter any sensible data in there, as everybody will be able to access them.

For more information on how to use the LabInform ELN from a user perspective, have a look at the [user manual](https://eln.docs.labinform.de/user/).


## Features

*A number of good reasons why to choose the LabInform ELN instead of other ELN candidates.*
System:

* Based on [DokuWiki](https://www.dokuwiki.org/), "a simple to use and highly versatile Open Source wiki software".
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
* Extensive documentation for [users](https://eln.docs.labinform.de/user/), [administrators]((https://eln.docs.labinform.de/admin/)), and [developers]((https://eln.docs.labinform.de/developer/))
* Large and vivid [DokuWiki](https://www.dokuwiki.org/) user community
* [DokuWiki](https://www.dokuwiki.org/) itself written in PHP, focussing on high code quality


## Non-Features

A few things the LabInform ELN does *not* provide/implement by purpose:

* Data store, aka repository\*
* Research data catalogue
* Management of measurement setups in the lab\*
* General project management, including proposals and publications\*
* General inventory for consumables
* Analysis workflow for data\*\*

The main reason lies in the "separation of concerns" (E. Dijkstra), focussing on one task at a time using one dedicated tool. Some of the "non-features" described above (and marked with an asterisk: *) are, however, part of the [wider LabInform LIMS](https://www.labinform.de/) the LabInform ELN is only one part of. If you are interested in a reproducible analysis workflow of spectroscopic data (**), have a look at the [ASpecD framework](https://docs.aspecd.de/) and related packages.


## Installation

Generally, DokuWiki requires a running web server and PHP, but no database. Hence, basic familiarity with setting up a web server and with the command line are necessary. The LabInform ELN builds upon a series of plugins for DokuWiki. Detailed installation instructions can be found in the [administrator manual](https://eln.docs.labinform.de/admin/).


## How to cite

The LabInform ELN is free software. However, if you use the LabInform ELN as crucial infrastructure component of your own research, please cite both, the article describing it and the software itself:

* Mirjam Schröder, Till Biskup. LabInform ELN: A lightweight and flexible electronic laboratory notebook for academic research based on the open-source software DokuWiki. *ChemRxiv*, 2023. doi:[10.26434/chemrxiv-2023-2tvct](https://doi.org/10.26434/chemrxiv-2023-2tvct)


## License

This program is free software: you can redistribute it and/or modify it under the terms of the **BSD License**. However, if you use the LabInform ELN as crucial infrastructure component of your own research, please cite it appropriately. See the "How to cite" section above for details.

Please note that DokuWiki itself is provided under a GNU General Public License (GPL). For details, see [their webpage](https://www.dokuwiki.org/faq%3Alicense). Most DokuWiki plugins are licensed under the GNU GPL as well, but please check yourself for each plugin you're using.
