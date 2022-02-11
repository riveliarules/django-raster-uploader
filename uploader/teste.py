import os
import werkzeug
from werkzeug.utils import secure_filename
from geo.Geoserver import Geoserver
import glob
from decouple import config

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.template import Context


geo = Geoserver(config('GS_HOST'), username=config('GS_USERNAME'),
                password=config('GS_PASSWORD'))

workspaces = geo.get_workspaces()['workspaces']
workspaces2 = geo.get_workspaces()['workspaces']['workspace']
print ("workspaces:", workspaces)
print ("workspaces2:", workspaces2)

ws = [workspace['name'] for workspace in  workspaces2]
print("usando for para popular a var ws, exibindo ws apos o for")
print(ws)

print("usando for para printar em linhas separadas cada item da var ws")
for item in ws:
    print(item)

exit()