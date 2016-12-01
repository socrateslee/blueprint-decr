#!/usr/bin/env python

long_description = ""

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except:
    pass

sdict = {
    'name': 'blueprint-decr',
    'version': "0.1.0",
    'license': 'MIT',
    'packages': ['blueprint_decr'],
    'zip_safe': False,
    'install_requires': ['six'],
    'long_description': long_description,
    'author': 'Lichun',
    'url': 'https://github.com/socrateslee/blueprint-decr',
    'classifiers': [
        'Environment :: Console',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python']
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**sdict)
