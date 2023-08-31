FAQ
=====

.. _faq:

.. _What's new in v4?:

What's new in v4?
----------------

difPy version 4 is the next-generation version of difPy, which not only achieves **up to 10x the performance** compared to version 3.x, but also comes with a variety of **new features** that make it's usage experience even better.

**Splitting of Processes**

difPy has been split into two main processes: first building the image repository with image tensors, and finally executing the search. This means that you will only have to build the image repository once, to then perform multiple search tests on the same repository.

For example, first we can build the ``dif`` object:

.. code-block:: python

   import difPy
   dif = difPy.build("C:/Path/to/Folder/")

And then we can perform two different searches on the same ``dif`` object:

.. code-block:: python

   search_duplicates = difPy.search(dif, similarity="duplicates")
   search_similar = difPy.search(dif, similarity= "similar")

**Multi Processing**

One of the most significant changes to version 4 is the implementation of multiprocessing. difPy leverages Python's multiprocessing capabilities for both the ``difPy.build`` part and the ``difPy.search`` part. This leads to massive performance increases on large datasets, especially for tasks like image tensor generation and computation of the MSEs.

In a test on a folder containing 6k images, including 3k duplicates, difPy needed on average 4min in total. Approximately 46% of total time were spent on building the image repository, and 55% on the search. That is 10x as fast as previous difPy versions on the same dataset.

**New Feature: In-Folder Search**

difPy now allows for searching for matches within folders separately, additionally to searching among the union of all images found. 

To highlight what this means in an example. If we had a folder structure as shown below:

.. code-block:: console

    .
    |- Folder1
    |  |-image1_1.jpeg
    |- Folder2
    |  |-image2_1.jpeg
    |-image.jpeg

We can run difPy on the main folder with the  :ref:`in_folder` parameter set to ``True``:

.. code-block:: python

   import difPy
   dif = difPy.build("C:/Path/to/Folder/")
   search = difPy.search(dif, in_folder=True)

difPy will then initiate a search for each separate folder considering them as separate search groups. It will search for matches among the main folder, in Folder1 and in Folder2.

**difPy is more Lightweight**

The difPy is now much more lightweight by depending less on external packages, and more on Python native features. Moreover, difPy processes certain functions more efficiently thanks to increased usage of `Numpy <https://www.geeksforgeeks.org/why-numpy-is-faster-in-python/>`_.

.. _Supported File Types:

Supported File Types
----------------

difPy supports most popular image formats. Nevertheless, since it relies on the Pillow library for image decoding, the supported formats are restricted to the ones listed in the `Pillow Documentation`_. Unsupported file types will by marked as invalid and included in the process statistics output under ``invalid_files`` (see :ref:`Process Statistics`).

.. _Pillow Documentation: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html

.. _Report a Bug:

Report a Bug 🐛
----------------

Should you encounter any issue or unwanted behavior when using difPy, `you can open an issue here <https://github.com/elisemercury/Duplicate-Image-Finder/issues/new/choose>`_.