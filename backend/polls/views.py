import time
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(f"Hello, world. You're at the polls index. Time is {time.strftime('%X')}.")
