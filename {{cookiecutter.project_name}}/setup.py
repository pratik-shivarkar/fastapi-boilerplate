"""
Copyright (C) Pratik Shivarkar - All Rights Reserved

This source code is protected under international copyright law.  All rights
reserved and protected by the copyright holders.
This file is confidential and only available to authorized individuals with the
permission of the copyright holders.  If you encounter this file and do not have
permission, please contact the copyright holders and delete this file.
"""


from setuptools import setup

setup(
    name='{{cookiecutter.project_name}}',
    version='0.1',
    py_modules=['manager.cli'],
    install_requires=[
        'asyncio==3.4.3',
        'cffi==1.14.5',
        'click==7.1.2',
        'colorama==0.4.4',
        'cryptography==3.4.7',
        'ecdsa==0.14.1',
        'fastapi==0.65.1',
        'greenlet==1.0.0',
        'h11==0.12.0',
        'h2==4.0.0',
        'hpack==4.0.0',
        'Hypercorn==0.11.2',
        'hyperframe==6.0.0',
        'orjson==3.5.1',
        'passlib==1.7.4',
        'priority==1.3.0',
        'psycopg2==2.8.6',
        'pyasn1==0.4.8',
        'pycparser==2.20',
        'pydantic==1.8.2',
        'python-dotenv==0.17.0',
        'python-jose==3.2.0',
        'python-json-logger==2.0.1',
        'python-multipart==0.0.5',
        'rsa==4.7.2',
        'six==1.15.0',
        'SQLAlchemy==1.4.6',
        'starlette==0.13.6',
        'toml==0.10.2',
        'typed-ast==1.4.3',
        'typing-extensions==3.7.4.3',
        'uvloop==0.15.2',
        'Werkzeug==1.0.1',
        'wsproto==1.0.0',
    ],
    entry_points='''
        [console_scripts]
        {{cookiecutter.project_name}}=manager.cli:cli
    ''',
)