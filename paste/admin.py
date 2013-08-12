#!/usr/bin/env python

from django.contrib import admin
from paste.models import Paste

class PasteAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title', 'created']
    # fields to filter the change list with
    list_filter = ['created']
    # fields to serch in change list
    search_fields = ['title', 'text']
    # enable the date drilldown on change list
    #date_hierarchy = 'created'
    # enable save button on top of change form
    save_on_top = True
    # pre-populate the slug from the title
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Paste, PasteAdmin)