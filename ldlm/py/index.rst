====================
Python Client
====================

.. |inline1| raw:: html

    <p>
    py-ldlm is an <a href="http://github.com/imoore76/ldlm" target="_blank">LDLM</a>
    client library providing Python sync and async clients at
    <a href="https://github.com/imoore76/py-ldlm" target="_blank">https://github.com/imoore76/py-ldlm</a>.
    </p>

|inline1|

Installation
--------------------

.. code:: shell

    $ pip install py-ldlm


Basic Usage
--------------------

Below are some basic usage examples. 

.. seealso::

    :doc:`LDLM Concepts</concepts>`
        For a basic understanding of how locks function and the different
        locking methods available.

    :doc:`LDLM Use Cases</uses>`
        For Python client examples of common use cases.

    :ref:`API Reference<py/index:api reference>`
        For a complete view of Python client functionality.


Client
^^^^^^^^^^^^^^
.. code-block:: python
    :caption: Create client

    import ldlm

    client = ldlm.Client("ldlm-server:3144")

.. code-block:: python
    :caption: Lock and unlock

    lock = client.lock("my-task")

    try:
        do_something()
    finally:
        lock.unlock()


.. code-block:: python
    :caption: Context manager

    # Lock will be unlocked when context manager exits
    with client.lock_context("my-task"):
        do_something()

Async Client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :caption: Create async client

    import ldlm

    client = ldlm.AsyncClient("ldlm-server:3144")

.. code-block:: python
    :caption: Async lock and unlock

    lock = await client.lock("my-task")

    try:
        await do_something()
    finally:
        await lock.unlock()


.. code-block:: python
    :caption: Async context manager

    # Lock will be unlocked when context manager exits
    async with client.lock_context("my-task"):
        await do_something()


TLS Configuration
--------------------

Using TLS for LDLM client connections involves passing a :ref:`ldlm.TLSConfig<py/index:TLS Config>` object to 
the client on instantiation.

.. code-block:: python
    :caption: Server TLS with cert signed by private CA

    import ldlm

    client = ldlm.Client("ldlm-server:3144", tls=ldlm.TLSConfig(
        ca_file="/etc/ldlm/certs/ca_cert.pem"
    ))

.. code-block:: python
    :caption: Mutual TLS

    import ldlm

    client = ldlm.Client("ldlm-server:3144", tls=ldlm.TLSConfig(
        cert_file="/etc/ldlm/certs/client_cert.pem",
        key_file="/etc/ldlm/certs/client_cert.pem",
        ca_file="/etc/ldlm/certs/ca_cert.pem"
    ))

.. seealso::

    Be sure to set up TLS in the server as described in :ref:`Server TLS<server/configuration:Server TLS>`.


API Reference
--------------------

.. autoclass:: ldlm.Client
   :members:
   :undoc-members:

.. autoclass:: ldlm.Lock
   :members:
   :undoc-members:

.. autoclass:: ldlm.AsyncClient
   :members:
   :undoc-members:

.. autoclass:: ldlm.AsyncLock
   :members:
   :undoc-members:

TLS Config
^^^^^^^^^^^^^^^^^^^
.. autoclass:: ldlm.TLSConfig
   :members:
   :undoc-members:

Exceptions
^^^^^^^^^^^^^^^^^^^

.. automodule:: ldlm.exceptions
   :members:
   :exclude-members: from_rpc_error
