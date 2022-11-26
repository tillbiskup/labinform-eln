====================
General organisation
====================

Of course, the wiki/ELN is yours, and it is entirely up to your liking how to structure and design your ELN. However, for those that never before worked with DokuWiki, this section will provide a few details. Ideally the result will be similar to how the demo installation available online via `<https://eln.labinform.de/>`_ looks like.

Note that DokuWiki uses a markup syntax special to this particular wiki. Basic familiarity with this syntax is assumed hereafter, and the official documentation available online provides excellent help and introduction. Therefore, the purpose of this and the following sections is to provide you with all the intricate details necessary to use a DokuWiki installation as an ELN, with template-based creation of pages via web forms and cross-linking capabilities.

First of all, DokuWiki is a hierarchical wiki, organising pages in namespaces (read: directories). Besides that, an ELN is one component of your laboratory knowledge management infrastructure. Hence, it should have an intuitive structure and provide easy access to all the necessary components. Therefore, a side bar with sensibly chosen links to the different parts of the ELN comes in quite handy, as well as overview pages and using icons for the different parts. Eventually, additional help texts that are hidden by default can be of great use for unexperienced or infrequent users. Explicitly documenting the seemingly obvious is often better than lacking required documentation.


Sidebar
=======

The sidebar cannot be edited directly, but you need to enter the name of the sidebar (by default, it is ``sidebar``) in the address line of your browser and afterwards create this page. In the example, the sidebar is divided into two sections, quick access and areas, with the former providing links to general pages and the latter giving an overview of the different areas of the ELN.


Main index
==========

The main index page contains both, a clickable overview of the areas as well as a folded explanation with more details. Using consistent (clickable) symbols (via the Icons plugin) for the different areas that are repeated both, in the sidebar and on the respective pages, helps users to easily access the area of interest. Using the wrap plugin allows for creating the large button-like patches representing the different areas. Note that the table of contents is actively suppressed on these overview pages. This is achieved using the special ``~~NOTOC~~`` directive at the top of the respective wiki page. For details of the implementation, have a look at the page source available online.


Foldable explanations
=====================

For each area there is a fold-out explanation at the top. This functionality is realized via the Folded plugin in combination with the Include plugin. In the demo installation available online, the correspondingly included page is called ``help``, is located in the same namespace (directory) as the associated area, and is included accordingly.

The explanations enable the users to familiarise themselves with the ideas behind it at any time or to get a well-founded overview during the first contact with the Wiki component of LabInform. Of course, as always, those who read, understand and implement the information will get the most out of it.
