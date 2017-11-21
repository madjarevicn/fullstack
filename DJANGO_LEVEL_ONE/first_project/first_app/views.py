# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#for home page method
def index(request):
    return HttpResponse("Hello world")


#this is method for help page - just testing
def help(request):
    return HttpResponse("This is help window")
