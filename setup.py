# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='order_management',
    version=version,
    description='Order Management for Bakery',
    author='Nishta Solutions',
    author_email='info@nishtasolutions.in',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
