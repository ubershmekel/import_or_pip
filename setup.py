#!/usr/bin/env python

#from distutils2.core import setup, find_packages
try:
    from setuptools import setup
    print('setuptools')
except ImportError:
    from distutils.core import setup
    print('distutils')

import import_or_pip

DOCUMENTATION = import_or_pip.__doc__


setup(name='import_or_pip',
      version='0.1',
      description="import a module or pip install it if it isn't found",
      long_description=DOCUMENTATION,
      keywords=['import', 'pip', 'download'],
      author='Yuval Greenfield',
      author_email='ubershmekel@gmail.com',
      home_page='http://yuvalg.com',
      license='Public Domain',
      test_suite='import_or_pip.test.test_import_or_pip',
      py_modules=['import_or_pip'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Terminals',
        ]
      )

