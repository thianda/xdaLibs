#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from setuptools import setup, find_packages
import sys
setup(
    name="xdaLibs",
    version="0.0.1",
    author="xda",
    author_email="thianda91@outlook.com",
    description="A helping-tool library for self-use",
    license="MIT",
    url="https://github.com/thianda/xdaLibs",
    packages=[
        'iniConfig'
    ],
    classifiers=[
        "Environment :: Web Environment",
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python :: 3',
    ],
    zip_safe=False,
    install_requires=[
        'configparser>=3.5.0'
    ]
)
