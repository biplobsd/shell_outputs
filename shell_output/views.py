from django.http import HttpResponse
from django.shortcuts import render
import operator
import os

def home(request):
    #watch -n 0 systemctl status gdrive
    r = os.popen('watch -n 0 systemctl status gdrive').read()
    return render(request, 'home.html',{'systemctlS':r})
