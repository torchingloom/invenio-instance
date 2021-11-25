# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 RSL.
#
# rsl is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Permissions for rsl."""

from invenio_access import Permission, any_user


def files_permission_factory(obj, action=None):
    """Permissions factory for buckets."""
    return Permission(any_user)
