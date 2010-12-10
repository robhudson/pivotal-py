==========
Pivotal-Py
==========

Pivotal-Py is a very thin wrapper built on top of `httplib2` to make requests
against the `Pivotal Tracker API`_.

.. _Pivotal Tracker API: http://www.pivotaltracker.com/help/api

Installation
============

Install from PyPI with ``easy_install`` or ``pip``::

    pip install pivotal-py

Dependencies
------------

Pivotal-Py requires `httplib2`_ 0.6.0 or later.

.. _httplib2: http://pypi.python.org/pypi/httplib2

Usage
=====

This Pivotal Tracker API client uses the token to authenticate with Pivotal
Tracker.  You can get a token by going to your user profile and creating an API
token.

Once you have an API token making requests against the APIs follows a simple
pattern of chainable methods, for example::

    from pivotal import Pivotal
    
    pv = Pivotal('TOKEN')
    
    # Assuming a base URL of 'http://www.pivotaltracker.com/services/v3/'
    
    # Perform a GET at /projects and processes content via ElementTree.
    etree = pv.projects().get_etree()

    # Perform the same GET at /projects but return the response and
    # content direct from httplib2.
    response, content = pv.projects().get()

Note: As seen above, there are two ways to get the content of a request:

    #. Call ``get_etree()`` to return the content as ElementTree object.

    #. Call ``get()`` to return the tuple containing both the response and
       content direct from httplib2.

Any positional arguments get pushed onto the URL::

    # Perform a GET at /projects/[id]/stories where [id] is a project ID.
    etree = pv.projects(id).stories().get_etree()

Any keyword arguments get mapped to the URL query string and appended at the
end of the URL::

    # Perform a GET at /projects/[id]/stories and filter stories by those that
    # are not started.
    etree = pv.projects(id).stories(filter='state:unstarted').get_etree()
    # Results in a URL of: /projects/[id]/stories?filter=state%3Aunstarted

Note: POSTs are currently not implemented, but the plan is to implement a
``post`` method that takes a body argument which is the body of the POST::

    # TODO: POST to /projects to create a new project
    etree = pv.projects().post(xml_body)


