from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home_page(request:HttpRequest):



    context ={}



    return render (request, 'main_app/home.html',context)