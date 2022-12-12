========
Workflow
========

Laboratory notebooks, whether paper-based or electronic, are an essential tool of scientific recordkeeping, *i.e.* documentation on a rather fundamental level. Only if we carefully document in sufficient detail what we have done, we and others can afterwards reproduce our results and follow our arguments and conclusions.

The basic idea behind the LabInform ELN is to provide a maximum of reproducibility and a good overview of what has been done in the laboratory, requiring a minimum of additional overhead. To this end, a workflow has been established that works well (from own experience over a decade) in a spectroscopic laboratory. Other laboratories may well have different needs and workflows, and due to the inherent flexibility of the DokuWiki engine underlying the LabInform ELN, you can adapt to your needs. Nevertheless, the details of the workflow developed by the authors of the LabInform ELN will be described in this user manual, together with the reasoning behind. This provides a solid basis for own adaptations and developments.


.. note::
    Actually, two workflows will be described: documenting measurements and dcumenting quantum-chemical calculations. The reason to show both is two-fold: (i) demonstrate the flexibility of the ELN approach chosen here, and (ii) the need for many spectroscopists to perform QC calculations to support the interpretation of their experimental results.

.. important::
    Here, the workflows are described on a more general (and abstract) level. For the details, such as the individual forms and the explanation for the fields they contain, see the respective individual pages of the user manual.


Documenting measurements
========================

As mentioned, the LabInform ELN has been developed in a spectroscopic laboratory. Hence, a guiding principle of the workflow described here is to document individual measurements in the necessary detail. This is clearly different, *e.g.*, from a synthetic laboratory where you will probably centre your workflow about syntheses. Nevertheless, it is clearly possible to use the LabInform ELN in a synthetic chemistry context as well and to implement the necessary processes in terms of an appropriate workflow.

The workflow described here for documenting (spectroscopic) measurements consists of three elements: an individual measurement is always performed on a sample, and a sample originates from a batch. While batches and samples strictly speaking belong to the inventory, documenting the individual measurements is at the heart of scientific recordkeeping and hence (electronic) laboratory notebooks.

.. figure:: ../images/workflow-measurement.png

    General workflow for documenting measurements: A measurement is always performed on a sample that in turn originates from a batch. Hence, to document a measurement, you first need to add a batch and a sample to the inventory and afterwards reference the sample in the measurement documentation.


Adding a batch and a sample to the inventory
--------------------------------------------

One of the operating principles of the LabInform ELN states that every measurement gets performed on a sample. Hence, before you can create a labbook entry (*i.e.*, a dedicated page containing information on a measurement), you should first add a sample to the inventory, in order to reference the sample from the labbook page.

Samples are the object that is investigated, *i.e.* in spectroscopy the entity that is put into the spectrometer. Each sample, in turn, originates from a batch, as usually, you will prepare the sample in some way or other, before it gets measured. In the simplest possible case, this preparation will be filling (parts of) the material of a batch in a tube or cell or other compartment used for measuring, or dissolving (and perhaps diluting) a batch in a solvent. As the two terms "sample" and "batch" are crucial, they will be defined below.


:Sample:
    The entity that gets investigated, result of some preparation starting with (parts of) a batch.

:Batch:
    Individual supply from collaborations, syntheses, or manufacturers; starting point of a sample.


For both, batches and samples, a minimum set of structured information (*i.e.* metadata) needs to be recorded. Therefore, web-forms are provided that ask the user of the LabInform ELN to enter this information. Furthermore, individual fields can be marked as optional.

Both batches and samples get assigned unique identifiers automatically. Here, integer numbers are used, in combination with an auto-increment. These numbers are used internally to cross-reference samples and batches, furthermore, a number is small enough to fit on any label of a sample or batch, regardless how small the sample (and label) will be.

While samples always originate from a batch, you can have situations where a batch originates from another batch. A typical example: You are provided with a batch in solid state, but need to dissolve it in some solvent in order to perform measurements on it. However, usually dissolving will result in more solution than you need for an individual sample. Therefore, you derive a batch in liquid state from a batch in solid state. To allow for this cross-referencing between batches, you can refer to an existing batch when creating an entry for a new batch.

Besides being necessary entries in the inventory for documenting measurements, the individual pages for batches and samples are the place to store any additional information that may seem relevant.


Creating a labbook entry for an individual measurement
------------------------------------------------------

The LabInform ELN is organised such that for each measurement on a sample, usually an individual labbook entry is created. To simplify creating labbook entries and to ensure a minimum consistent set of metadata, web-forms are provided. These metadata are shown as a table on top of each labbook entry, and hence as a rule of thumb, as soon as one of these parameters changes, you should create a new labbook entry (*i.e.*, wiki page) - and perhaps cross-reference from and to the entry before.

An important field that shall not be underestimated is "purpose": Usually you have an idea why you perform a measurement, at least at the time of data acquisition. Recording this information and including it into an overview table of measurements can help dramatically with finding the relevant labbook entry.

Next to the metadata forming the header of the labbook entry is a detailed chronological protocol of what has been done. Not only the start and end of a measurement should be recorded. Often it does matter when the measurement device and the cooling system (if applicable) have been switched on, and there will be many more details worth mentioning.

Besides metadata and a chronological protocol, it has been proven useful to add generic graphical representations of the recorded data to the labbook pages after the data have been analysed or at least initially processed. You can automate this process as much as possible, even adding the figures from your analysis software by using the API of the wiki engine. However, it is not necessary to fully automate the process, but rather to be aware of the advantage generic graphical representations in the labbook can have.

Another aspect that proved to be very useful is to document all relevant metadata obtained during data acquisition. As these metadata should be available in machine-readable form independent of the ELN, storing them in structured text files is a simple yet powerful solution. To this end, a file format (termed infofile format) has been developed by the authors of LabInform ELN. These files can simply be added to the labbook page in a way they can be downloaded as individual file. Thus, you can document these important metadata once and store them in several places, once on the file system next to the acquired actual data, and once in the ELN.


Documenting (quantum-chemical) calculations
===========================================

While documenting measurements in a laboratory has long been (and in many cases still is) the realm of paper-based laboratory notebooks, documenting (quantum-chemical) calculations is a somewhat different matter, as the entire process of performing these calculations is usually completely digital. Therefore, it is much more obvious to document the process digitally as well.

Similarly to the workflow described above for documenting measurements, the workflow for documenting calculations consists of three individual elements: molecules, geometries, and actual calculations. While there can and usually will exist several geometries of the same molecule, calculations are always performed on a given geometry. The result of a calculation can be a different geometry (in case of geometry optimisations and alike) or parameters, or both.


.. figure:: ../images/workflow-calculation.png

    General workflow for documenting quantum-chemical calculations: Calculations are performed on geometries that belong to a molecule. There can (and usually will) be more than one geometry for a molecule. The results of calculations can be new geometries, parameters, or both.


