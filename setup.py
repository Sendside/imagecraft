#!/usr/bin/env python
import os
from distutils.core import setup

# Figure out the version; this could be done by importing the
# module, though that requires Django to be already installed,
# which may not be the case when processing a pip requirements
# file, for example.
import re
here = os.path.dirname(os.path.abspath(__file__))
version_re = re.compile(
    r'__version__ = (\(.*?\))')
fp = open(os.path.join(here, 'imagecraft', '__init__.py'))
version = None
for line in fp:
    match = version_re.search(line)
    if match:
        version = eval(match.group(1))
        break
else:
    raise Exception("Cannot find version in __init__.py")
fp.close()


def find_packages(root):
    # so we don't depend on setuptools; from the Storm ORM setup.py
    packages = []
    for directory, subdirectories, files in os.walk(root):
        if '__init__.py' in files:
            packages.append(directory.replace(os.sep, '.'))
    return packages


setup(
    name = 'imagecraft',
    version=".".join(map(str, version)),
    description = 'Simple framework that uses PIL to colorize and sandwich '\
        'images together to quickly create colorized graphics.',
    author = 'Kevin Williams',
    author_email = 'kevin@isolationism.com',
    license = 'BSD',
    url = 'https://github.com/isolationism/imagecraft',
    classifiers = [],
    packages = find_packages('imagecraft'),
    install_requires = ['pil'],
)
