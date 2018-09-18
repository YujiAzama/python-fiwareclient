# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name="fiwareclient",
    version="0.1.0",
    packages=find_packages(),
    author="Yuji Azama",
    author_email="yuji.azama@gmail.com",
    entry_points={
        'console_scripts': [
            'fiware = fiwareclient.shell:main',
        ],
        'fiwareclient.command': [
            'entity-list=fiwareclient.orion.cmd:EntityList',
            'entity-create=fiwareclient.orion.cmd:EntityCreate',
            'entity-delete=fiwareclient.orion.cmd:EntityDelete',
            'attribute-data-get=fiwareclient.orion.cmd:AttributeDataGet',
        ],
    },
    test_suite='fiwareclient/tests'
)
