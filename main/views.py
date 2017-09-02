from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User,UserManager,AbstractBaseUser
from django.contrib.auth import authenticate,login,logout
from Login.models import UserProfile
from .models import Purchase,Items

def index(request):
	user = request.user
	u = UserProfile.objects.filter(user = user)
	if len(u) > 0:
		if (u[0].typid=="Student"): 
			return redirect('/main/disp')
		elif(u[0].typid=="Mess Worker"):
			item = Items.objects.all
			return render(request,'main/test1.html',{'item':item})
	else:
		raise Http404

def add(request):
	if  request.method == 'POST':
		regno = request.POST['regno']
		item = request.POST['item']
		quant = int(request.POST['quant'])
		q=Items.objects.filter(name=item)
		perprice=int(q[0].price)
		price1 = (quant * perprice)
		m=UserProfile.objects.filter(regno = regno)
		t=m[0].extras
		print(t)
		print(" Hello ")
		price2=t+price1
		print(price2)
		pur = Purchase(regno=regno,item=item,quantity=quant,price=price1)
		pur.save()
		use = UserProfile.objects.filter(regno = regno).update(extras =price2)
		return render(request,'main/show.html',{'item':item,'quant':quant,'pur':pur})
	else:
		raise Http404


def disp(request):

	u=request.user
	us = UserProfile.objects.filter(user = u)
	ext = us[0].extras
	regno = us[0].regno
	rec = Purchase.objects.filter( regno = regno)
	return render(request,'main/list.html',{'rec':rec,'ext':ext})


def wrong(request):

	gi = request.GET.get('gi')
	m=Purchase.objects.filter(id = gi)
	r=m[0].regno
	p=m[0].price
	u=UserProfile.objects.filter(regno = r)
	p1=u[0].extras
	p2=(p1-p)
	use = UserProfile.objects.filter(regno = r).update(extras=p2)
	Purchase.objects.filter(id = gi).delete()
	return render(request,'main/add.html')



# Create your views here.
