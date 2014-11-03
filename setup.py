#!/usr/bin/env python
from setuptools import setup
from os import path

README = path.join(path.dirname(__file__), "README.rst")
with open(README) as f:
    LONG_DESCRIPTION = f.read()


def get_version(filename):
    """
    Parse the value of the __version__ var from a Python source file
    without running/importing the file.
    """
    import re
    version_pattern = r"^ *__version__ *= *['\"](\d+\.\d+\.\d+)['\"] *$"
    match = re.search(version_pattern, open(filename).read(), re.MULTILINE)

    assert match, ("No version found in file: {!r} matching pattern: {!r}"
                   .format(filename, version_pattern))

    return match.group(1)


setup(
    name="ucam-timetable-engineering-utils",
    version=get_version("engineering_to_tt.py"),
    description=(
        "A command line program to convert Engineering's iCalendar feeds into "
        "Timetable's XML import format."),
    author="Hal Blackburn",
    author_email="hwtb2@cam.ac.uk",
    url="https://github.com/ucamhal/ucam-timetable-engineering-utils",
    entry_points = {
        'console_scripts': [
            'engineering-to-tt = engineering_to_tt:main'
        ],
        "ttapiutils.autoimport.datasources": [
            "engineering = engineering_to_tt:data_source_factory"
        ]
    },
    py_modules=['engineering_to_tt'],
    install_requires=[
        "docopt>=0.6.2",
        "icalendar>=3.7",
        "ipython>=2.1.0",
        "lxml>=3.3.5",
        "pytz>=2014.4",
        "ucam-timetable-api-utils>=0.0.1"
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
