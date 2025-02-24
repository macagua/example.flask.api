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

    $ flask --app hello run

Open a new terminal windows for testing the API using a HTTP client
as `curl <https://curl.se/>`_ command.


----


Make requests
=============

The ``curl`` command allows you to quickly test an API from the terminal without
the need for having to download a specific application.


request POST json format
-------------------------

.. code-block:: console

    $ curl -X POST http://localhost:5000/create -H "Content-Type: application/json" -d '{"name": "John Doe", "address": "123 Main St"}'


request GET with response 200
-----------------------------

.. code-block:: console

    $ curl -X GET http://127.0.0.1:5000/


request GET with response 200
-----------------------------

.. code-block:: console

    $ curl -X GET http://127.0.0.1:5000/detail/4


request PUT json format
------------------------

.. code-block:: console

    $ curl -X PUT http://127.0.0.1:5000/update/4 -H "Content-Type: application/json" -d '{"name": "Jane Doe", "address": "456 Elm St"}'


request DELETE
---------------

.. code-block:: console

    $ curl -X DELETE http://127.0.0.1:5000/delete/4


This way I make the API requests using the ``curl`` command.

----

References
==========

- `Quickstart — Flask documentation <https://flask.palletsprojects.com/en/stable/quickstart/>`_.
