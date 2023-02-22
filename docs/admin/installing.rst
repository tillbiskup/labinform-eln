===================
Installing DokuWiki
===================

Installing DokuWiki requires a webserver and access to the underlying operating system as an administrator. Once having setup the ELN, there should be no need any further to access the file system, as anything should be controllable via the DokuWiki web interface. However, during installation a few things can only be done with direct access to the file system that require basic familiarity with the command line and web servers.

This section will provide some advice with installing the DokuWiki base and the required plugins. Creating the first content and organising your wiki will be covered in the following sections. As installing the DokuWiki requires access on the operating-system level, you may seek help from your IT department or skilled colleagues for this part. This is particularly true for the base installation and the special configurations requiring files to be copied on the file system.


Base wiki
=========

For general instructions of how to install DokuWiki, see the `official installation instructions available online <https://www.dokuwiki.org/install>`_. Generally, system requirements of the DokuWiki are quite low, only a webserver and PHP are necessary. Basic configuration of the freshly installed DokuWiki is done using a web interface. Usually, you will want to set the wiki as a "closed wiki", with every access requiring a user account.

After having installed a bare DokuWiki, you need to add a number of plugins. This can be done from the DokuWiki admin interface via a web browser or from the command line with file system access to the server. The latter is only suggested for experienced users or if you intend to automate the installation. For details, see the respective section of the `official DokuWiki manual available online <https://www.dokuwiki.org/plugin_installation_instructions>`_.

For a complete list of plugins that should be installed and a short description of their use within the ELN, see :numref:`tab-plugins`

.. table:: DokuWiki plugins necessary for using the wiki as ELN. The plugin names are given as specified in the official DokuWiki documentation available online, hence the inconsistent spelling/captalisation. Each plugin can be found by the given name and installed via the plugin manager available from the DokuWiki admin interface.
    :name: tab-plugins

    =========================== =================================================================================
    Name                        Description
    =========================== =================================================================================
    Bureaucracy                 Web forms used to create pages, *e.g.*, for the lab notebook

                                and the inventory (samples, batches)
    Structured Data             Collecting and storing structured data (metadata) on individual wiki pages;

                                allows to aggregate information in overview tables and lists with filters
    sqlite                      Interface to an SQLite database used solely for easier access to the data

                                collected using the Structured Data plugin and contained in individual

                                wiki pages
    templatepagename            Access to template files from within the wiki interface using special

                                (and configurable) names
    Definition List             Used for the protocol on the individual lab notebook pages providing

                                a detailed list of tasks carried out prefixed with timestamps
    caption                     Figure and table captions, including referencing these captions
    Wrap                        Structure a wiki page, *e.g.*, multiple columns and button-like areas
    Icons                       Include fontawesome and other icons into wiki pages,

                                helpful for easier navigation and overview
    configuration file manager  Access to the configuration files from within the DokuWiki admin area
    folded                      Create folded parts of a page, *e.g.*, for help texts
    include                     Include other pages into a wiki page; used for help texts

                                in conjunction with the folded plugin
    Note                        Simple way to add highlighted notes to wiki pages
    tplinc                      Conditionally include pages at certain parts of the DokuWiki template;

                                useful, *e.g.*, for area-specific additional navigation in the sidebar
    upgrade                     Upgrade the DokuWiki from within the admin interface
    snippets                    Insert templates into the current page at the cursor position

                                helpful for more consistent documentation, reusing well-crafted

                                building blocks
    (bibtex)                    not available via extension manager, needs rewrite and renaming
    =========================== =================================================================================


General configuration
=====================

There is a series of general configuration settings that should be changed from their defaults. This again can be done using the DokuWiki admin interface via a web browser. For details of the configuration settings to be changed and their respective values, see :numref:`tab-configuration`.


.. table:: Configuration settings of a DokuWiki installation used as ELN. The configuration is grouped into \dokuwiki-specific and plugin-specific sections, and the former into separate blocks. Each configuration setting has a unique key that is given in small print on the configuration page. ``check`` and ``uncheck`` refer to checkboxes and their respective state.
    :name: tab-configuration
    :width: 100%

    +--------------+-------------------+-------------------+
    | Block        | Key               | Setting           |
    +==============+===================+===================+
    | **DokuWiki**                                         |
    +--------------+-------------------+-------------------+
    | Basic        | start             | index             |
    |              +-------------------+-------------------+
    |              | dmode             | 0750              |
    |              +-------------------+-------------------+
    |              | fmode             | 0640              |
    +--------------+-------------------+-------------------+
    | Display      | breadcrumbs       | 0                 |
    |              +-------------------+-------------------+
    |              | youarehere        | check             |
    |              +-------------------+-------------------+
    |              | toptoclevel       | 2                 |
    |              +-------------------+-------------------+
    |              | useheading        | Wiki Content Only |
    +--------------+-------------------+-------------------+
    | Advanced     | userewrite        | .htaccess         |
    |              +-------------------+-------------------+
    |              | useslash          | check             |
    +--------------+-------------------+-------------------+
    | **Plugins**                                          |
    +--------------+-------------------+-------------------+
    | Data         | edit_content_only | check             |
    +--------------+-------------------+-------------------+
    | Include      | showfooter        | uncheck           |
    |              +-------------------+-------------------+
    |              | showdate          | uncheck           |
    |              +-------------------+-------------------+
    |              | showuser          | uncheck           |
    |              +-------------------+-------------------+
    |              | showcomments      | uncheck           |
    |              +-------------------+-------------------+
    |              | showlinkbacks     | uncheck           |
    |              +-------------------+-------------------+
    |              | showtags          | uncheck           |
    |              +-------------------+-------------------+
    |              | showeditbtn       | uncheck           |
    +--------------+-------------------+-------------------+
    | Snippets     | snips_updatable   | uncheck           |
    |              +-------------------+-------------------+
    |              | old_revisions     | uncheck           |
    |              +-------------------+-------------------+
    |              | userreplace       | uncheck           |
    +--------------+-------------------+-------------------+

Of course, you can deviate from some of the settings given here without impairing functionality, as some are merely a matter of personal taste. Nevertheless, others are necessary for the DokuWiki to work as intended.

The ``start``, ``userewrite``, and ``useslash`` settings ensure the DokuWiki URLs to behave like ordinary URLs, given the appropriate configuration of your webserver, including rewrite rules.

``breadcrumbs``, ``youarehere``, ``toptoclevel``, and ``useheading`` are mainly a matter of taste, whereas the last configuration setting is crucial to have sensible information in the aggregation tables for labbook pages.

The ``edit_content_only`` setting of the Structured Data Plugin should be enabled, as otherwise, users editing the data tables will always be confronted with a rather complex form that allows for both, editing the values of the respective fields as well as their types. The latter, however, is neither necessary nor helpful to ensure consistency throughout your ELN.



Special configurations
======================

The tplinc plugin needs some special attention, as by default, the standard template provided by DokuWiki does not support the include hooks. Therefore, according to the documentation of the tplinc plugin available online, you need to copy the configuration provided by the plugin to the global configuration file directory. Assuming a unixoid-like operating system, you would issue the following command from within the DokuWiki root directory:

.. code-block:: bash

    cp lib/plugins/tplinc/dokuwiki/* conf/


Once done, in the special admin section for the tplinc plugin, you can include wiki pages at specific places of the template. Within the ELN, this is used as area-specific additional navigation in the sidebar.


