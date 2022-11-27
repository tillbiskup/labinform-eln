Workflow
========

The basic idea behind the LabInform ELN is to provide a maximum of reproducibility and a good overview of what has been done in the laboratory, requiring a minimum of additional overhead. To this end, a workflow has been established that works well (from own experience over a decade) in a spectroscopic laboratory. Other laboratories may well have different needs and workflows, and due to the inherent flexibility of the DokuWiki engine underlying the LabInform ELN, you can adapt to your needs. Nevertheless, the details of the workflow will be described in this user manual, together with the reasoning behind. This provides a solid basis for own adaptations and developments.


.. note::
    There are two workflows that eventually need to be described: measurements and quantum-chemical calculations. The reason to show both is two-fold: (i) demonstrate the flexibility of the ELN approach chosen here, and (ii) the need for many spectroscopists to perform QC calculations to support the interpretation of their experimental results.

.. todo::
    Further flesh out the workflow aspects below and move them to individual pages each.


Adding a sample to the inventory
================================

One of the operating principles of the LabInform ELN states that every measurement gets performed on a sample. Hence, before you can create a labbook entry (*i.e.*, a dedicated page containing information on a measurement), you should first add a sample to the inventory, in order to reference the sample from the labbook page.

Samples are the object that is investigated, *i.e.* in spectroscopy the entity that is put into the spectrometer.

Each sample, in turn, originates from a batch, as usually, you will prepare the sample in some way or other, before it gets measured.


Creating a labbook entry
========================

The LabInform ELN is organised such that for each measurement on a sample, usually an individual labbook entry is created. To ease creating labbook entries, web forms are provided.

