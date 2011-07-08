CHANGES
=======

0.1.3 (2011-07-08)
------------------

- Removed Pivotal import from __init__.py which was causing httplib2
  issues.

0.1.2 (2011-07-08)
------------------

- Added ``httplib2`` as a dependency.

0.1.1 (2010-12-10)
------------------

- Added an examples folder with a single example showing a script to send
  an email summarizing stories across projects to multiple team members.

- Provide both ``get()`` and ``get_etree()``.  The ``get()`` method
  returns the response and content of the request directly from httplib2.
  The ``get_etree()`` will return an ElementTree object of the content.

0.1.0 (2010-10-15)
------------------

- Initial public release.

