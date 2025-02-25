=================
example.flask.api
=================

.. image:: https://raw.githubusercontent.com/macagua/example.flask.api/master/docs/_static/flask-vertical.png
   :class: image-inline

Building an API application with Flask and SQLAlchemy.


Requirements
============

Please execute the following commands:

::

    $ sudo apt install -y python3-dev python3-pip python3-virtualenv
    $ sudo apt install -y git
    $ git clone https://github.com/macagua/example.flask.api.git flask-api
    $ cd ./flask-api
    $ virtualenv --python /usr/bin/python3 venv
    $ source ./venv/bin/activate
    $ pip3 install -U pip
    $ pip3 install -r requirements.txt


----


Running
=======

Please execute the following command:

::

    $ flask run

Open a new terminal windows for testing the API using a HTTP client
as `curl <https://curl.se/>`_ command.


----


Make requests
=============

The ``curl`` command allows you to quickly test an API from the terminal without
the need for having to download a specific application.


request GET with response 200
-----------------------------

.. code-block:: console

    $ curl -X GET http://127.0.0.1:5000/

The above command demonstrates how to perform a ``GET`` method to get the users registered
by default in the database as a ``READ`` operation into a ``CRUD`` application.

request POST json format
-------------------------

.. code-block:: console

    $ curl -X POST http://localhost:5000/create -H "Content-Type: application/json" -d '{"name": "John Doe", "address": "123 Main St"}'

The command above demonstrates how to perform a ``POST`` method with a ``json`` format.
That is, it is actually inserting a new user into the database  as a ``CREATE`` operation
into a ``CRUD`` application.

request GET with response 200
-----------------------------

.. code-block:: console

    $ curl -X GET http://127.0.0.1:5000/detail/4

The above command demonstrates how to perform a ``GET`` method to get the detailed
information of the user with the id ``4`` as a ``READ`` operation into a ``CRUD`` application.

request PUT json format
------------------------

.. code-block:: console

    $ curl -X PUT http://127.0.0.1:5000/update/4 -H "Content-Type: application/json" -d '{"name": "Jane Doe", "address": "456 Elm St"}'

The above command demonstrates how to perform a ``PUT`` method with a ``json`` format.
That is, it is actually updating the user information with the id ``4``  as a ``UPDATE``
operation into a ``CRUD`` application.

request DELETE
---------------

.. code-block:: console

    $ curl -X DELETE http://127.0.0.1:5000/delete/4

The above command demonstrates how to perform a ``DELETE`` method with a ``json`` format.
That is, you are actually deleting the information of the user with the id ``4`` as a
``DELETE`` operation into a ``CRUD`` application.

This way I make the API requests using the ``curl`` command.


----

Testing
=======

To run the tests, please execute the following command:

::

    $ pytest -v


This way you can check that the application is working correctly.


----


License
========

This project is licensed under the MIT License - see the `LICENSE <./LICENSE>`_ file for details.


----


References
==========

- `Quickstart — Flask documentation <https://flask.palletsprojects.com/en/stable/quickstart/>`_.
- `SQLAlchemy Unified Tutorial <https://docs.sqlalchemy.org/en/20/tutorial/index.html#unified-tutorial>`_.
- `Testing Flask Applications — Flask documentation <https://flask.palletsprojects.com/en/stable/testing/>`_.
