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

from django.contrib import admin

from .models import *

__author__ = 'Emanuele Bertoldi <emanuele.bertoldi@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015, django ERP Team'
__version__ = '0.0.1'


class RegionAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'slug')
    prepopulated_fields = {"slug": ("title",)}


class PluggetAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'description', 'slug')
    search_fields = ('title', 'slug')


admin.site.register(Region, RegionAdmin)
admin.site.register(Plugget, PluggetAdmin)
