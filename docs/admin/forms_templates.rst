===================
Forms and templates
===================

Key to using DokuWiki as an electronic laboratory notebook (ELN) is to use forms and templates for creating most of the content. This ensures consistency and allows for automatic cross-linking of content. For the forms, three plugins are used that work together seamlessly:

  * Bureaucracy Plugin
  * Structured Data Plugin
  * sqlite plugin


The Bureaucracy Plugin is responsible for creating the web forms, while the Structured Data Plugin allows for depositing information in a structured way as key-value pairs that can be aggregated and filtered afterwards. This allows, *inter alia*, to automatically create overview tables of all measurements performed with a certain sample (on the respective sample page), or an overview of all measurements of a certain kind (see below for details).

One note regarding the use of the Structured Data Plugin: While there is a "spiritual successor" of this plugin by the same author (A. Gohr, the main author and maintainer of DokuWiki), the Structured Data Plugin does not rely on a database for its primary data storage. This is a big advantage, as all content is contained solely in the DokuWiki pages (aka bare text files on the file system). Internally, the plugin uses an SQLite database via the sqlite plugin, but this is only for faster access and simpler internal usage. This means that you can safely ignore the SQLite DB (*e.g.*, not including it in a backup) without loosing any functionality or content (this is probably not entirely true regarding the field aliases, though).


Forms
=====

  * required and optional fields; presets

  * field aliases via Structured Data Plugin

  * additional fields depending on one form field

  * selecting templates depending on one form field

  * alternative labels for fields



Templates
=========

  * data table at the top

  * field aliases via Structured Data Plugin

  * empty entries for optional fields

  * automatic cross-linking via interwiki links\ [#note]_

  * preventing automatic replacement when creating data tables


The two general ways templates can be used in DokuWiki

  * templates for each new page in a namespace (use the templatepagename plugin for direct user access to the respective template)
  * templates via web forms (Bureaucracy Plugin)



Overview tables
===============


  * selecting type of entry and fields displayed

  * filtering (including omitting templates)

  * sorting


Footnotes
=========

.. [#note] Is it possible to setup interwiki links from within the admin interface? Yes, using the ``configuration file manager`` plugin