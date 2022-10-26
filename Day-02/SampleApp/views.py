from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
	return HttpResponse("Good Afternoon to All..")

def sample(r):
	return HttpResponse("<h2>Good Afternoon to All..</h2>")

def hrf(self,aq):
	return HttpResponse("<h2>Hi Welcome {}!!</h2>".format(aq))

def stdnt(request,y,r,k="CSE"):
	return HttpResponse("Student Roll Number is: {}<br/>Year is: {}<br/>Your Branch is: {}".format(r,y,k))


