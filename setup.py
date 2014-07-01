#!/usr/bin/env python
from setuptools import setup
from os import path

README = path.join(path.dirname(__file__), "README.rst")
with open(README) as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="ucam-timetable-engineering-utils",
    version="0.1.0",
    description=(
        "A command line program to convert Engineering's iCalendar feeds into "
        "Timetable's XML import format."),
    author="Hal Blackburn",
    author_email="hwtb2@cam.ac.uk",
    url="https://github.com/ucamhal/ucam-timetable-engineering-utils",
    entry_points = {
        'console_scripts': [
            'engineering-to-tt = engineering_to_tt:main'
        ]
    },
    py_modules=['engineering_to_tt'],
    requires=[
        "docopt (>=0.6.2)",
        "icalendar (>=3.7)",
        "ipython (>=2.1.0)",
        "lxml (>=3.3.5)",
        "pytz (>=2014.4)"
    ],
    license="BSD",
    classifiers=[
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Topic :: Internet :: WWW/HTTP",
    ],
    long_description=LONG_DESCRIPTION,
)
