#!/usr/bin/env python
from __future__ import division, absolute_import, print_function,\
    unicode_literals
import sys
from distutils.core import setup

if sys.version_info < (2, 6):
    print("Sorry, this only works on Python 2.6+, 3+")
    sys.exit(1)


setup(name='anaconda-clean',
      version='1.0',
      author='Continuum Analytics',
      license='BSD',
      description='Delete Anaconda config files',
      py_modules=['anaconda_clean'],
      )
