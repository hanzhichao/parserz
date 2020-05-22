#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""
import os
from setuptools import setup, find_packages

this_directory = os.path.abspath(os.path.dirname(__file__))
setup_requirements = []


def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(
    author="Han Zhichao",
    author_email='superhin@126.com',
    description='Easy parser for parse template $variable',
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",  # 新参数
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],
    license="MIT license",
    include_package_data=True,
    keywords=[
        'parserz', 'parser', 'dollar parser',
    ],
    name='parserz',
    packages=find_packages(include=['parserz']),
    setup_requires=setup_requirements,
    url='https://github.com/hanzhichao/parserz',
    version='0.13',
    zip_safe=True,
    install_requires=['pyyaml', 'jsonpath']
)
