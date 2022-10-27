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

def wg(g):
	return HttpResponse("<html><head><title>Demo</title></head><body><h3>Sample response by using html structure</h3></body></html>")

def dgh(q,qw):
	return HttpResponse("<html><head><title>Demo</title></head><body><h3>Hi Welcome <span style='color:cadetblue'>{}</span></h3></body></html>".format(qw))

def ae(t,nm):
	return HttpResponse("<html><head><title>Demo</title><style>span{color:yellow}</style></head><body><h3>Hi Welcome <span>"+nm+"</span></h3></body></html>")

def jy(request):
	return HttpResponse("<html><head><title>Demo for Javascript</title><script>alert('Welcome to this site')</script></head><body><h3>Sample Example for Javascript</h3></body></html>")

def cy(request,k):
	return HttpResponse("<html><head><title>Demo for Javascript</title><script>alert('Welcome User {}')</script></head><body><h3>Hi User {}</h3></body></html>".format(k,k))

def gk(request):
	return render(request,'sample.html')

def vy(request,qy):
	return render(request,'demo.html',{'p':qy})

def std(request):
	return render(request,'strg.html')

def me(request):
	if request.method == "POST":
		name = request.POST['en']
		eid = request.POST['ei']
		eg = request.POST['ea']
		return render(request,'edetails.html',{'ename':name,'empid':eid,'eage':eg})
	return render(request,'employee.html')





