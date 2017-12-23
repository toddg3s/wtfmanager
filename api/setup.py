# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "stablemanager"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Willow Tree Farm Horse Management API",
    author_email="todd@willowtree.farm",
    url="",
    keywords=["Swagger", "Willow Tree Farm Horse Management API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    long_description="""\
    This API provides information about horses being boarded at Willow Tree Farm
    """
)

