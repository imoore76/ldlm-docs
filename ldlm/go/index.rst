=================
Go Client
=================


.. |inline1| raw:: html

    <p>
    A Go <a href="http://github.com/imoore76/ldlm" target="_blank">LDLM</a> client library
    at <a href="http://github.com/imoore76/ldlm/client" target="_blank">http://github.com/imoore76/ldlm/client</a>.
    </p>

|inline1|

Installation
===============

.. code-block:: go

    // your go application
    include "github.com/imoore76/ldlm/client"

then

.. code-block:: bash

    $ go mod tidy


Basic Example
==================

.. code-block:: go

    import (
        "context"

        "github.com/imoore76/ldlm/client"
    )

    c, _ := client.New(context.Background(), client.Config{
        Address: "ldlm-server:3144",
    })

    lock, err := c.Lock("my-task", nil)

    if err != nil {
        panic(err)
    }

    func() {
        defer lock.Unlock()
        doMyTask()
    }()

.. seealso::

    :doc:`LDLM Concepts</concepts>`
        For a basic understanding of how locks function and the different
        locking methods available.

    :doc:`LDLM Use Cases</uses>`
        For Python client examples of common use cases.

    :ref:`API Reference<py/index:api reference>`
        For a complete view of Python client functionality.


Usage
==================

.. |apidocs| raw:: html

    <a href="https://pkg.go.dev/github.com/imoore76/ldlm/client" target="_blank">pkg.go.dev</a>

.. |dialopts| raw:: html

    <a href="https://pkg.go.dev/google.golang.org/grpc#DialOption" target="_blank">dial options</a>

Comprehensive Go module documentation is available at |apidocs|.

Create a Client
--------------------
A client takes a context and a :ref:`Config<go/index:Client Config>` object.
You can Cancel the context to abort a client's operations.

.. code-block:: go

    c, err := client.New(context.Background(), client.Config{
        Address: "localhost:3144",
    })

    if err != nil {
        panic(err)
    }

``New()`` also takes an arbitrary number of
gRPC |dialopts|
that are passed along to ``grpc.Dial()``.

Client Config
++++++++++++++++++

A ``Config{}`` object should be supplied to :ref:`New()<go/index:Create a client>`.

.. code-block:: go

    type Config struct {
        Address     string // host:port address of ldlm server
        NoAutoRenew bool   // Don't automatically renew locks before they expire
        UseTls      bool   // use TLS to connect to the server
        SkipVerify  bool   // don't verify the server's certificate
        CAFile      string // path to file containing a CA certificate
        TlsCert     string // path to file containing a TLS certificate for this client
        TlsKey      string // path to file containing a TLS key for this client
        Password    string // password to send
        MaxRetries  int    // maximum number of retries on network error or server unreachable
    }

Lock Object
--------------------

``Lock`` objects are returned from successful
:ref:`Lock()<go/index:Lock()>` and :ref:`TryLock()<go/index:TryLock()>` client methods.

.. code-block:: go

    type Lock struct {
        Name   string // The name of the lock
        Key    string // The name of the lock
        Locked bool   // Whether the lock was acquired or not
    }

.. option:: func (l *Lock) Unlock() error

    Unlocks the lock.

Lock Options
--------------------

Lock operations take a ``*LockOptions`` object that specifies
relevant lock options.

.. code-block:: go

    type LockOptions struct {
        WaitTimeoutSeconds int32 // How long to wait for the lock to become available
        LockTimeoutSeconds int32 // How long to hold the lock before needing to renew
        Size               int32 // Size of the lock
    }

.. note::

    These options are described in more detail in
    :doc:`LDLM Concepts</concepts>`.

Lock()
--------------

.. option:: func (c *Client) Lock(name string, options *LockOptions) (*Lock, error)

``Lock()`` attempts to acquire a lock in LDLM. It will block until the lock is acquired or until ``WaitTimeoutSeconds`` has elapsed (if specified).
It accepts the following arguments:


.. list-table::
    :header-rows: 1

    * - Type
      - Description
    * - ``string``
      - Name of the lock to acquire
    * - ``*LockOptions``
      - Options for the lock

It returns a ``*Lock`` and an ``error``.

Examples
++++++++++++++

.. code-block:: go
    :caption: Simple lock

    lock, err = c.Lock("my-task", nil)
    if err != nil {
        // handle err
    }

    func() {
        defer lock.Unlock()
        doWork("my-task")
    }()

.. code-block:: go
    :caption: Wait timeout

    lock, err = c.Lock("my-task", &client.LockOptions{WaitTimeoutSeconds: 5})
    if err != nil {
        panic(err)
    }

    if !lock.Locked {
        fmt.Println("Couldn't obtain lock within 5 seconds")
        return
    }

    func() {
        defer lock.Unlock()
        doWork("my-task")
    }()



TryLock()
-----------------

.. option:: func (c *Client) TryLock(name string, options *LockOptions) (*Lock, error)

``TryLock()`` attempts to acquire a lock and immediately returns;
whether the lock was acquired or not. You must inspect the
returned lock's ``Locked`` property to determine if it was acquired.

``TryLock()`` accepts the following arguments.

.. list-table::
    :header-rows: 1

    * - Type
      - Description
    * - ``string``
      - Name of the lock to acquire
    * - ``*LockOptions``
      - Options for the lock

It returns a ``*Lock`` and an ``error``.

Examples
+++++++++++++

.. code-block:: go
    :caption: Simple try lock

    lock, err = c.TryLock("my-task", nil)
    if err != nil {
        // handle err
    }
    if !lock.Locked {
        // Something else is holding the lock
        return
    }

    func() {
        defer lock.Unlock()
        doWork("my-task")
    }()

Errors
----------------

The following errors may be returned from lock operations and correspond
to :ref:`LDLM API errors<server/api:API Errors>` of the same name.

* ``ErrLockDoesNotExist``
* ``ErrInvalidLockKey``
* ``ErrLockWaitTimeout``
* ``ErrLockNotLocked``
* ``ErrLockDoesNotExistOrInvalidKey``
* ``ErrInvalidLockSize``
* ``ErrLockSizeMismatch``
