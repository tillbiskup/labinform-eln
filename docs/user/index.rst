========
Overview
========

This user manual addresses the **users of the LabInform ELN**, *i.e.* the people working in the lab, using the ELN as a tool for their daily work. While the underlying DokuWiki provides you with a lot of flexibility in how you arrange and organise the individual entries, changing templates and forms according to the needs are the responsibility of administrators and are hence described in the :doc:`administrator manual </admin/index>`.


Prerequisites
=============

This user manual assumes a **working installation of the LabInform ELN** to be available. In case you need to first install the LabInform ELN, see the :doc:`administrator manual </admin/index>`.

Furthermore, **basic familiarity with the formatting syntax of Dokuwiki** is assumed, as each individual page (be it for labbook entries, samples, or else) is a wiki page using the DokuWiki markup. Those new to DokuWiki may have a look at the `excellent official documentation of the DokuWiki syntax <https://www.dokuwiki.org/wiki:syntax>`_.


Scope
=====

Each ELN needs to be adapted to the special needs of the individual scientist or work group. To do so, you need to understand the processes in your lab in a detail that allows you to model them in an electronic workflow such as an ELN. Hence, there is **no turnkey solution** that works out of the box. Having that said, this documentation (and particularly this user manual section) focusses on the functionality as provided by the `demo instance <https://eln.labinform.de/>`_ available online (https://eln.labinform.de/).

Therefore, this user manual will guide you through the different aspects of the LabInform ELN demo instance, explaining the workflow and the ideas behind. Note that different areas of the ELN purposefully use different solutions to similar problems to demonstrate the approaches available.


Contents
========

Overview
--------

  * :doc:`Workflow <workflow>`

    The overall workflow of the LabInform ELN as implemented in the demo instance and used in the authors' lab is described. For details of the individual aspects, refer to the sections of the manual referenced below.


Experimental work: (spectroscopic) measurements of samples
----------------------------------------------------------

  * :doc:`Batches <batches>`

    All measurements are carried out on samples that in turn are derived from batches. A batch can be the individual supply from collaborations, syntheses, or manufacturers and is the starting point of a sample.

  * :doc:`Samples <samples>`

    All measurements are carried out on samples. Here, the term refers to the actual entity that gets investigated and that is the result of some preparation starting with (parts of) a batch.

  * :doc:`Measurements <measurements>`

    As the LabInform ELN is developed from spectroscopists and (not only) for spectroscopists, the actual measurement (*i.e.*, experiment) and its appropriate documentation is a central aspect of the ELN. All measurements are carried out on samples.


.. todo::
    Add syntheses here as an additional, rather special workflow; mention at least sample containers (cells, tubes) and substrates.


Theoretical work: (quantum-chemical) calculations
-------------------------------------------------

  * :doc:`Molecules <molecules>`

    Calculations are performed on geometries that belong to a molecule. Therefore, one molecule can have many associated geometries. In the easiest and most obvious case, you start with a non-optimised geometry assembled in some program and afterwards run a geometry optimisation. Other reasons for several geometries are conformations and isomers, as well as different spin multiplicities or explicit enviroments that will lead to (slightly) different geometries as well.

  * :doc:`Geometries <geometries>`

    Calculations are performed on geometries that belong to a molecule. Hence, a geometry always belongs to a molecule, while the same molecule may have several different geometries (see above).

  * :doc:`Calculations <calculations>`

    Calculations are performed on geometries and may result in new geometries (in case of a geometry optimisation) or, more general, in a list of properties of the molecule, be it a transition dipole moment or magnetic resonance parameters, to name but a few.

