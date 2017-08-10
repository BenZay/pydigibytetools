#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='digibyte',
      version='1.1.25',
      description='Python Digibyte Tools',
      author='Esotericizm',
      author_email='esotericizm@cryptoservices.net',
      url='http://github.com/Digitools/pydigibytetools',
      install_requires='six==1.8.0',
      packages=['digibyte'],
      scripts=['pybtctool'],
      include_package_data=True,
      data_files=[("", ["LICENSE"])],
      )
