#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/10/21 17:39'

from django.forms import forms


class FileUploadForm(forms.Form):
    my_file = forms.FileField()