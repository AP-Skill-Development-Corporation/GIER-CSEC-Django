from django.shortcuts import render,redirect
from . forms import UsReg
from django.contrib import messages
from django.contrib.auth.decorators import login_required
 
# Create your views here.
@login_required
def home(request):
	return render(request,'html/home.html')

def register(request):
	if request.method == "POST":
		f = UsReg(request.POST)
		if f.is_valid():
			f.save()
			messages.success(request,"User Created Successfully")
			return redirect('/login')
	f = UsReg()
	return render(request,'html/register.html',{'v':f})