# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 RSL.
#
# rsl is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""RSL"""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('rsl', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='rsl',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='rsl Invenio',
    license='MIT',
    author='RSL',
    author_email='atlantij@gmail.com',
    url='https://github.com/rsl/rsl',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'rsl = invenio_app.cli:cli',
        ],
        'invenio_base.apps': [
            'rsl_records = rsl.records:rsl',
        ],
        'invenio_base.blueprints': [
            'rsl = rsl.theme.views:blueprint',
            'rsl_records = rsl.records.views:blueprint',
        ],
        'invenio_assets.webpack': [
            'rsl_theme = rsl.theme.webpack:theme',
            'rsl_search_app = rsl.records.webpack:search_app',
        ],
        'invenio_config.module': [
            'rsl = rsl.config',
        ],
        'invenio_i18n.translations': [
            'messages = rsl',
        ],
        'invenio_base.api_apps': [
            'rsl = rsl.records:rsl',
         ],
        'invenio_jsonschemas.schemas': [
            'rsl = rsl.records.jsonschemas'
        ],
        'invenio_search.mappings': [
            'records = rsl.records.mappings'
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
