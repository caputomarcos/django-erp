#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""This file is part of the django ERP project.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from djangoerp.settings.base import (
    DEBUG,
    TEMPLATE_CONTEXT_PROCESSORS,
    MIDDLEWARE_CLASSES
)

__author__ = 'Emanuele Bertoldi <emanuele.bertoldi@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015, django ERP Team'
__version__ = '0.0.1'

AUTH_USER_MODEL = 'core.User'

LOGIN_URL = '/users/login'
LOGOUT_URL = '/users/logout'
LOGIN_REDIRECT_URL = '/'

LOGIN_REQUIRED_URLS = (
    r'/(.*)$',
)

LOGIN_REQUIRED_URLS_EXCEPTIONS = (
    r'/static/(.*)$',
    r'/users/login/$',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'djangoerp.core.context_processors.auth',
    'djangoerp.core.context_processors.system_info',
)

##Middleware classes
MIDDLEWARE_CLASSES += (
    'djangoerp.core.middleware.RequireLoginMiddleware',
    'djangoerp.core.middleware.LoggedInUserCacheMiddleware',
)

# List of middleware classes to use.  Order is important; in the request phase,
# this middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
AUTHENTICATION_BACKENDS = (
    'djangoerp.core.backends.ModelBackend',
    'djangoerp.core.backends.ObjectPermissionBackend',
)

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

BREADCRUMBS_DEFAULT_TEMPLATE = "partials/breadcrumbs.html"
