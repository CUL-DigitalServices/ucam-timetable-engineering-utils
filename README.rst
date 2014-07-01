README
======

This repo contains a hastily written program to convert Cambridge University
Engineering Department's iCalendar teaching event data into the import
("API") format used by Timetable (timetable.cam.ac.uk).

Usage
-----

Install the package with pip, for example::

  $ pip install git+https://github.com/ucamhal/ucam-timetable-engineering-utils.git

Alternatively, ``requirements.txt`` lists the (Python package) dependencies. Assuming they're installed (``$ pip install -r requirements.txt``) the ``engineering_to_tt.py`` file can be executed directly.


Run ``fetch_calendar_data.sh`` to pull down Engineering IA-IIB's calendar data,
then run::

  $ engineering-to-tt -s substitutions.example.json -t engineering-test data/*/*.ics > engineering-test.xml

``engineering-test.xml`` will contain the data for all 4 parts under a tripos
named "engineering-test".

Assuming the tripos exists and you have sufficient permissions to edit all 4
parts, you can import the data at ``https://$DOMAIN/api/v0/xmlimport``.
