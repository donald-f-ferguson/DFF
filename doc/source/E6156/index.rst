.. _ref_e6156:


.. toctree::
   :maxdepth: 1
   :hidden:

==========
E6156
==========

This section provides an overview of the PyAnsys Geometry library,
explaining key concepts and approaches for primitives,
sketches (2D basic shape elements), and model designs.



PyAnsys Geometry overview
=========================

PyAnsys Geometry is a Python wrapper for the Ansys Geometry service.
Here are some of the key features of PyAnsys Geometry:

* Ability to use the library alongside other Python libraries
* A *functional-style* API for a clean and easy coding experience
* Built-in examples

Simple interactive example
==========================
This simple interactive example shows how to start an instance of
the Geometry server and create a geometry model.

Start Geometry server instance
------------------------------

The :class:`Modeler() <ansys.geometry.core.modeler()>` class
within the ``ansys-geometry-core`` library creates an instance of
the Geometry service. By default, the ``Modeler`` instance connects to
``127.0.0.1`` (``"localhost"``) on port ``50051``. You can change this
by modifying the ``host`` and ``port`` parameters of the ``Modeler`` object,
but note that you must also modify your ``docker run`` command by changing
the ``<HOST-PORT>:50051`` argument.

This code starts an instance of the Geometry service:



Create geometry model
---------------------

Once an instance has started, you can create a
geometry model by initializing the :ref:`sketch <ref_sketch>` subpackage and using the
:ref:`shapes <ref_primitives>` subpackage.




