from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    return render(request,'Main_page.html')

def birjaBhai(req):
    return render(req,'birja.html')