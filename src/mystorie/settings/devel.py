# -*- coding: utf-8 -*-
"""
Django development settings for soo project.
"""
from . import *


# Debug
DEBUG = True

TEMPLATE_DEBUG = DEBUG


# Application definition
INSTALLED_APPS += (
    'debug_toolbar',
)


MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


# Debug toolbar
INTERNAL_IPS = ('10.0.2.2',)
