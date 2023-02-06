#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name="query_athena",
    version='0.1',
    description='Package for running queries on athena',
    url='https://github.com/affinityanswers/query-athena', 
    packages=['query_athena'],
    scripts = ['scripts/query_athena'],
    install_requires=['pyathena', 'awscli']
)
