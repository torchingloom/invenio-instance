# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 RSL.
#
# rsl is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Pytest fixtures and plugins for the UI application."""

import pytest
from invenio_app.factory import create_ui


@pytest.fixture(scope='module')
def create_app():
    """Create test app."""
    return create_ui