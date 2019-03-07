# coding: utf-8

"""
    Harmony Connect

    An easy to use API that helps you access the Factom blockchain.  # noqa: E501

    OpenAPI spec version: 1.0.17
    Contact: harmony-support@factom.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "harmony-connect-client"
VERSION = "1.0.7"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Harmony Connect",
    author_email="harmony-support@factom.com",
    url="https://github.com/FactomProject/factom-harmony-connect-python-client",
    keywords=["factom", "factom-blockchain", "blockchain", "blockchain-as-a-service", "client-library", "Harmony Connect"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
=============================
Harmony Connect Client
=============================

Harmony Connect is your fast lane to the blockchain. Add blockchain capabilities to any software without needing to wrestle with currencies, wallets, or blockchain nodes. Instead, you get easy read and write access to the Factom blockchain. Connect will also track your data's path to immutability and will notify you along the way.


============
Requirements
============

Python 2.7 and 3.4+

====================
Installation & Usage
====================

***********
pip install
***********

You can install the package hosted on PyPi by using pip:

``pip install harmony_connect_client``

Then import the package:
``import harmony_connect_client``


You can also install the Harmony Connect client directly from Github


``pip install git+https://github.com/FactomProject/factom-harmony-connect-python-client.git``

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/FactomProject/factom-harmony-connect-python-client.git`)

**********
Setuptools
**********

Install via `Setuptools <http://pypi.python.org/pypi/setuptools>`_.


``python setup.py install --user``

(or `sudo python setup.py install` to install the package for all users)

Then import the package:
``import harmony_connect_client``

=============================
Harmony Connect Documentation
=============================
This client is built to communicate with Factom Harmony Connect. For more information about using this API, please visit the Harmony Connect `documentation <https://docs.harmony.factom.com>`_.

You can create a free account at `Factom.com <https://account.factom.com>`_.
    """
)
