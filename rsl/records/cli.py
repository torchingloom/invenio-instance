# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Command Line Interface for accounts."""

from __future__ import absolute_import, print_function

from functools import wraps

import click
from flask import current_app
from flask.cli import with_appcontext
from flask_security.forms import ConfirmRegisterForm
from flask_security.utils import hash_password
from werkzeug.datastructures import MultiDict
from werkzeug.local import LocalProxy


@click.group()
def rsl():
    """RSL commands."""
