================
Usage
================

LDLM server is distributed with 2 programs:

* :ref:`ldlm-server<server/usage:server>` - the main LDLM server
* :ref:`ldlm-lock<server/usage:lock tool>` - lock manipulation tool

Server
------------

Start the LDLM server with

.. code-block:: text

    ldlm-server --listen_address=0.0.0.0:3144

.. seealso::

    See :ref:`command line options<server/configuration:options>` 
    and ``ldlm-server --help``.


Lock Tool
------------------

The ``ldlm-lock`` command is used to manipulate locks in a running LDLM server on the CLI.
It must be run on the same environment (machine, container, et al.) as a running LDLM server

.. seealso::

    See :ref:`IPC configuration<server/configuration:IPC Socket File>`
    and ``ldlm-lock --help``

Commands
^^^^^^^^^^^^^^^

.. option:: ldlm-lock list
    
    This prints a list of locks and their keys.

.. option:: ldlm-lock unlock <lock name>
    
    Force unlocks the lock named by **<lock name>**.

