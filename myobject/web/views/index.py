# -*- coding: utf-8 -*-
# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return	HttpResponse("网站Web前台首页！")