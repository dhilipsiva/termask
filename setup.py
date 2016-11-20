#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: setup.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-11-20
"""

from setuptools import setup, find_packages
from codecs import open

__VERSION__ = '0.1.2'

setup(
    name='termask',
    version=__VERSION__,
    description='A curses-based python library & terminal utility to ask questions and get answers in a wizardly fashion.',
    url='https://github.com/dhilipsiva/termask',
    author='dhilipsiva',
    author_email='dhilipsiva@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console :: Curses',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],

    keywords='termask terminal ask question answers curses wizard',
    packages=find_packages(),
    py_modules=['termask'],
    entry_points='',
    install_requires=open('requirements.txt', 'r').read().splitlines(),
    package_data={
        '': ['*.txt'],
    },
    include_package_data=True,
)

