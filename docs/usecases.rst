=========
Use cases
=========

To give you a first impression of how working with the LabInform ELN may look like and what tasks you can perform using an ELN, a series of high-level use cases is provided. These use cases are informed by the longstanding experience of the authors of the LabInform ELN and hence rooted within the setting of a spectroscopy lab dealing with sometimes rather complex (non-routine) measurements of individual samples.

.. note::

    The use cases described here are on a rather abstract level, describing overall tasks to be performed with an ELN. The details of how to achieve these tasks within the LabInform ELN are provided in the :doc:`user manual <user/index>`.

Basically, there are two groups of use cases, one for documenting experiments carried out on physical samples, the other documenting (quantum-chemical) calculations. However, eventually both scenarios have rather similar requirements and hence use cases.

Typical use cases regarding the **documentation of experiments** and getting access to the information contain:

  * :ref:`Document an individual measurement of a sample <sec-usecases_labbook_entry>` (*i.e.*, a single labbook entry)
  * :ref:`Get an overview of all the measurements performed on a particular sample <sec-usecases_measurements4sample>`
  * :ref:`Get an overview of all the measurements performed with a method, sortable and with filtering capabilities <sec-usecases_measurements4method>`


Similarly, if it comes to **documenting (quantum-chemical) calculations**, you will be interested in the following use cases:

  * Document an individual calculation on a given geometry of a molecule
  * Get an overview of all calculations performed on a particular geometry
  * Get an overview of all available geometries of a particular molecule

Each of these are described in some detail below. For getting an idea how these use cases are actually implemented in the LabInform ELN and how to use this ELN, have a look at the :doc:`user manual <user/index>`.


.. _sec-usecases_labbook_entry:

Document an individual measurement of a sample
==============================================

Documenting individual measurements is at the heart of scientific recordkeeping and has a direct parallel in the analog world of a paper-based lab notebook. To achieve a maximum of reproducibility, you would like to document exactly what has been done. Usually, this includes a series of structured metadata (*e.g.* sample, date, operator, type of measurement, purpose) that can be stored as key--value pairs as well as a detailed chronological protocol of the individual tasks performed and observations made. Furthermore, you can add media (typically images or graphical representations of data) and other information, as well as comments and (first) analyses of the data.


.. todo::
    Add figure here with two panels comparing (made-up) paper-based labbook entry with (made-up) ELN entry, to compare both, but to make it somewhat accessible?


Some of the big advantages of electronic lab notebooks compared to their analog paper-based counterpart include: They can be easily searched, they allow to provide templates for more homogeneous and complete documentation, and they can contain (clickable) links to the data and other digital research artifacts.


.. _sec-usecases_measurements4sample:

Overview of all measurements performed on one sample
====================================================

Particularly in spectroscopy, you often perform more than one measurement on the same sample, as you intend to get the maximum information and samples can be quite expensive an hence valuable. Therefore, a typical use case is to get an overview of all measurements that have been performed on an individual sample. Getting not only the list of measurements, but as well the purpose of each individual measurement (and perhaps an indicator of its success) would be even better.

In an analog paper-based labbook, this can only be achieved by carefully keeping a manual list of these measurements, and even then this list would not be sortable according to your needs that may well differ depending on the question you have.

With an ELN, all this can be achieved much more easily, given that the necessary information is available as structured metadata (think of key--value pairs). In the LabInform ELN, each individual labbook entry comes with a series of structured metadata such as the sample identifier that can be used to create overview tables, *e.g.*, listing all measurements that have been performed on one sample. Furthermore, you are free to add any other information to these overview tables that is available as structured metadata.


.. _sec-usecases_measurements4method:

Overview of all measurements performed with one method
======================================================

Similarly to getting an overview of all measurements performed on an individual sample, sometimes it is very helpful to get a list of all measurements performed with a method. This overview should of course not only contain a link to the individual labbook entry, but as well to the overview page of the sample measured (that in turn should contain a list of all measurements performed with it).

One of the big advantages of an ELN compared to the analogue paper-based approach is exactly these cross-links that allow you to access a wealth of information from different directions. Sometimes we remember to have run an experiment, but are not necessarily sure which sample was involved, or we want to look for a comparable measurement on a different sample. In this case, the overview of all measurements performed using a certain method is helpful. Allowing to apply filters and being sortable adds to the value of these tables as an overview and way to access the wealth of information contained in the individual labbook pages.

Of course, a labbook is only as valuable as the information you put into it. But making this information easily accessible is an additional motivation to enhance the quality of your documentation. While our future self is usually the first person profiting from properly documenting what we have done, reproducibility requires us to document in ways others can make sense of. Therefore, every tool that helps and motivates us to improve our way of scientific recordkeeping eventually enhances the quality of the science we're performing.


And some use cases for QC calculations:

  * Document an individual calculation on a given geometry of a molecule
  * Get an overview of all calculations performed on a particular geometry
  * Get an overview of all available geometries of a particular molecule


.. todo::
    Document use cases for QC calculations

