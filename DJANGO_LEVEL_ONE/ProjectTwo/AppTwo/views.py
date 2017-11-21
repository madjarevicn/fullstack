# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me':'Oh!I am injected from views.py'}
    return render(request,'AppTwo/index.html',context=my_dict)

def help(request):
    my_dict = {'insert_me':"OH. I am injected from views.py"}
    return render(request,'AppTwo/help.html',context=my_dict)
