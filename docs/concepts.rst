========
Concepts
========

The concepts described below are not unique to the LabInform ELN, but in their entirety they make the LabInform ELN standing out from other similar solutions. Thus, they answer the question what makes the LabInform ELN different and why it is worth considering it -- and the underlying principles. As said, concepts are much more important than concrete implementations, as long as they get implemented in a working piece of software.

  * Small footprint: minimum system requirements, simple installation, no database backend
  * Wiki-based: simple, yet powerful markup; high flexibility
  * Entries are created by web forms and based on templates
  * Help texts are included right into the ELN
  * Inventory: Samples and batches
  * Usually one labbook entry per measurement
  * Measurements are grouped by method
  * Labbook entries contain crucial metadata
  * Labbook entries are cross-referenced from the sample pages
  * Most adjustments can be made from *within* the Web UI


Small footprint
===============

A labbook, and for the sake of argument an ELN, is a tool you want to use daily. Hence it should be robust, resilient, and not depend on any unnecessary external infrastructure. Furthermore, the easier an ELN is to setup, the more likely is it to be adopted by groups or individual researchers that lack either or both of personal IT experience and IT support.

Hence, the LabInform ELN comes with minimum minimum system requirements thanks to the underlying `DokuWiki wiki engine <https://www.dokuwiki.org/>`_ it is based upon. It is quite simple to install, requiring nothing more than a web server and PHP. Particularly and quite in contrast to most other wiki engines, DokuWiki does not require a database backend. You could even install DokuWiki (and hence the LabInform ELN) on a memory stick for a maximum of independence and portability. If interested, see the official `DokuWiki on a Stick <https://www.dokuwiki.org/install:dokuwiki_on_a_stick>`_ documentation.


Wiki-based
==========

minimum system requirements, simple installation, no database backend

existing wiki software, battle-proven, much larger user base than any ELN


Web forms and templates
=======================

Entries are created by web forms and based on templates


Help included
=============

Help texts are included right into the ELN, in a way they don't disturb the frequent user but help those unfamiliar or only occasionally using the system.


Inventory for samples
=====================

Inventory: Samples and batches

.. note::
    An inventory is not a key component of an ELN. Furthermore, the inventory shown here is mostly restricted to samples and does *not* include consumables in general. Inventories for consumables and particularly for chemicals have some requirements and constraints that are clearly out of scope of the LabInform ELN.


Grouping by method
==================

Measurements are grouped by method


One page per measurement
========================

Usually one labbook entry per measurement


Metadata and (automatic) cross-referencing
==========================================

  * Labbook entries contain crucial metadata
  * Labbook entries are cross-referenced from the sample pages


Adjustments from within the Web UI
==================================

  * Most adjustments can be made from *within* the Web UI
  * No detailed IT know-how (server, terminal) and no access to the file system necessary

