========
Concepts
========

The concepts described below are not unique to the LabInform ELN, but in their entirety they make the LabInform ELN standing out from other similar solutions. Thus, they answer the question what makes the LabInform ELN different and why it is worth considering -- even more so the underlying principles. As said, concepts are much more important than concrete implementations, as long as they do get implemented in a working piece of software.


  * Small footprint: minimum system requirements, simple installation, no database backend
  * Wiki-based: simple, yet powerful markup; high flexibility
  * Entries are created by web forms and based on templates
  * Help texts are included right into the ELN
  * Inventory: Samples and batches
  * Usually one labbook entry per measurement
  * Measurements are grouped by method
  * Labbook entries contain crucial metadata
  * Labbook entries are cross-referenced from the sample pages and *vice versa*
  * Recurring blocks of a labbook entry can be inserted using templates
  * Most adjustments can be made from *within* the Web UI


Small footprint
===============

A labbook, and for the sake of argument an ELN, is a tool you want to use daily. Hence it should be robust, resilient, and not depend on any unnecessary external infrastructure. Furthermore, the easier an ELN is to setup, the more likely it is to be adopted by groups or individual researchers that lack either or both of personal IT experience and IT support.

Hence, the LabInform ELN comes with minimum system requirements thanks to the underlying `DokuWiki wiki engine <https://www.dokuwiki.org/>`_ it is based upon. It is quite simple to install, requiring nothing more than a web server and PHP. Particularly and quite in contrast to most other wiki engines, DokuWiki *does not require a database backend*. You could even install DokuWiki (and hence the LabInform ELN) on a memory stick for a maximum of independence and portability. If interested, see the official `DokuWiki on a Stick <https://www.dokuwiki.org/install:dokuwiki_on_a_stick>`_ documentation.


Wiki-based
==========

The LabInform ELN is wiki-based, providing all the advantages of wikis, such as a simple, yet powerful markup and a high flexibility regarding the actual content, including media and alike. What is even more: the LabInform ELN does not reinvent the wheel but is based on existing wiki software, namely `DokuWiki <https://www.dokuwiki.org/>`_, that is battle-proven and particularly suited for documentation and knowledge management. Furthermore, an existing wiki software provides a much larger user base than any ELN. The larger a user base, particularly for open-source software, the more robust and mature, and the higher the chance for long-term availability.


Web forms and templates
=======================

While a wiki provides the necessary flexibility to record all relevant information, a labbook and particularly an ELN should be structured to allow for a straight-forward access to the valuable information stored within. Particularly in an ELN, structured metadata allow to aggregate information, thus providing an overview and simple access. Therefore, in the LabInform ELN, entries are usually created by web forms and based on templates.


Help included
=============

Systems that are used regularly should have a user interface that is as intuitive as possible. Nevertheless, while we can try to minimise accidental complexity as much as possible, every non-trivial process comes with inherent complexity we have to cope with. In terms of an ELN, those originally designing and regularly using it don't need any manual. However, usually you will have some people new to the lab or only temporarily present that are going to use the ELN, and others may only use it infrequently. While in-person training to get people started is highly valuable, being the single point of contact for all questions regarding a praticular tool doesn't scale well. This is why in the LabInform ELN, help texts are included right into the ELN, in a way they don't disturb the frequent user but help those unfamiliar or only occasionally using the system. Here, both brief and to the point explanations of how to perform the task at hand as well as (lab-specific) conventions shall be provided.


Inventory for samples
=====================

While technically not a key component of an ELN, the inventory for samples serves a key function in the LabInform ELN, adding much to reproducibility. Each sample is given a unique identifier (in case of the LabInform ELN a simple number), and each measurement is performed on a sample. This allows to automatically cross-reference samples and measurements (see below). Furthermore, by providing an individual page for every sample you can store all relevant information regarding a sample at a dedicated place.

Actually, the inventory is organised in a slightly more advanced way: While a sample is the actual object a measurement is performed on, each sample in turn originates from a batch. In most cases there will be more material than what ends up in a sample, be it a stock solution or else. Furthermore, in case of collaborations batches are what usually is provided by the collaboration partners, and samples the entities prepared for the dedicated individual measurement. Batches can originate from batches as well, to cope with typical situations such as dissolving a solid material in some solvent. Of course, batches and samples get automatically cross-referenced with each other.


.. note::
    An inventory is not a key component of an ELN. Furthermore, the inventory shown here is mostly restricted to samples and does *not* include consumables in general. Inventories for consumables and particularly for chemicals have some requirements and constraints that are clearly out of scope of the LabInform ELN.


Grouping by method
==================

Due to originating from a spectroscopic lab, the LabInform ELN is organised around measurements on samples, hence focussing largely on processes. For a better overview, the measurements are grouped by individual method. How you define an individual method depends on the local needs and constraints. Generally, if two measurements require different kinds of general metadata, they likely belong to different methods. To give a few examples: In NMR spectroscopy, high-resolution and solid-state NMR will be two different methods. In EPR spectroscopy, cw-, time-resolved, and pulsed EPR will belong to different methods. In optical spectroscopy, steady-state and time-resolved measurements clearly belong to different methods, as do absorption and fluorescence spectroscopy. Sometimes you will perform more than one method on the same sample, but thanks to the sample inventory, you can create individual labbook pages for each measurement and not loosing overview due to the automatic cross-referencing.


One page per measurement
========================

As mentioned above, the LabInform ELN is organised around measurements on samples. Usually, you will create one labbook entry per measurement. Exceptions from this rule are repeated measurements on the identical sample with identical conditions that directly follow on each other. Similarly, short experiments to optimise parameters will usually be documented on the same page as the final "real" measurement. As a rule of thumb, as soon as you need to change the metadata for a measurement that are part of the structured metadata block at the beginning of each page (for details see below), you want to create a new labbook entry, using the web form as described above.


Metadata and (automatic) cross-referencing
==========================================

Lab notebooks are an established tool for scientific recordkeeping, and acquiring relevant information in form of (structured) metadata is a crucial aspect of documenting the research process. Therefore, each labbook entry contains crucial metadata. At least some of this relevant information is grouped in a block of structured metadata in form of key--value pairs, residing at the top of the individual page. This allows for aggregating this information in overview tables that are sortable and can be filtered.

Furthermore, labbook entries for individual measurements are cross-referenced from the sample pages and *vice versa*. Thus, the LabInform ELN provides different ways to access the relevant information. You can either start with a particular sample and see on its page in the inventory what measurements have been performed, as this information is automatically available in an overview table cross-linked to the individual labbook entries. Similarly, you can start with a method, have a look at the measurements that have been performed, look at an individual measurement and from there continue to the sample.

The cross-references just mentioned are added automatically, thanks to using web forms for creating entries for samples and measurements. Additionally, the LabInform ELN simplifies manual cross-references by providing special markup for linking to samples, batches, and alike, once again making use of functionality provided by the underlying `DokuWiki wiki engine <https://www.dokuwiki.org/>`_.


Recurring blocks of a labbook entry via templates
=================================================

Often, certain recurring elements need to be added to a labbook page, be it a step in a synthesis or another metadata file containing all metadata recorded *during* data acquisition. This is possible from within the DokuWiki editor using a template manager. The templates as such can be fully controlled by the individual users and previewed within the template manager.


Adjustments from within the Web UI
==================================

Another strength of the `DokuWiki wiki engine <https://www.dokuwiki.org/>`_, besides its simple usage, robustness, and small footprint: most adjustments can be made from *within* the Web UI. The same is true therefore for the LabInform ELN. Web forms and templates are entirely created using the Web UI, and even moving individual pages as well as larger chunks of content is possible, besides configuring nearly every aspect of the wiki engine.

As a consequence, operating and adjusting the LabInform ELN does *not* require any detailed IT know-how (server, terminal) nor access to the file system. This is particularly helpful for small groups or situations with limited IT capacities. Additionally, due to the minimal system requirements, maintenance of the underlying operating system can be limited to a minimum as well.

