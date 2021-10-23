from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request,*args,**kwargs):
	return render(request,'index.html',{})

def login(request,*args,**kwargs):
	return render(request,'login.html',{})



def register(request,*args,**kwargs):
	return render(request,'signup.html',{})
