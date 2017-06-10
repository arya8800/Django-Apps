import logging
from django.template import Context, loader
from django.db.models import Max
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseNotFound
from django.template import RequestContext,loader
from gonextmedia.models import *
from gonextmedia.forms import *
from django.shortcuts import render_to_response
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

logged_id=-1

def index(request):
	global logged_id
	logged_id=-1
	user_name="helo"
	return render(request,'index.html',{'user_name':user_name})
	
def kyc(request):
	return render(request,'kyc.html')

def manage(request):
	return render(request,'manage-compane.html')
	
def myprofile(request):
	return render(request,'my-profile.html')
	
def network(request):
	return render(request,'network.html')
	
def payout(request):
	return render(request,'payouthitory.html')
	
def promotional(request):
	return render(request,'Promotional.html')
	
def reffral(request):
	return render(request,'reffral.html')
	
def rewards(request):
	return render(request,'rewards.html')
	
def sales(request):
	return render(request,'sales.html')
	
def todayt(request):
	return render(request,'today-task.html')

@csrf_exempt	
def front(request):
	return render_to_response ('login.html')

@csrf_exempt	
def signup(request):
	form = user(request.POST or None)
	if form.is_valid():
		a=account.objects.get_or_create(first=form.cleaned_data['firstname'], email=form.cleaned_data['email'])
	variables = RequestContext(request,{'form':form})
	return render_to_response ('signup.html',variables)
	
	