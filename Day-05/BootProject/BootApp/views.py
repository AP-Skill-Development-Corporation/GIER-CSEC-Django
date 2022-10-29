from django.shortcuts import render,redirect
from .models import Note
# Create your views here.
def home(request):
	return render(request,'home.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def noteall(request):
	h = Note.objects.all()
	if request.method == "POST":
		sb = request.POST['sn']
		title = request.POST['tt']
		dec = request.POST['ds']
		b = Note(nsubject=sb,ntitle=title,ndesc=dec)
		b.save()
		return redirect('/notes')
	return render(request,'note.html',{'n':h})

def noteup(request,h):
	c = Note.objects.get(id=h)
	if request.method == "POST":
		c.nsubject = request.POST['snup']
		c.ntitle = request.POST['ttup']
		c.ndesc = request.POST['dsup']
		c.save()
		return redirect('/notes')
	return render(request,'noteupdate.html',{'k':c})

def notedlt(request,p):
	g = Note.objects.get(id=p)
	if request.method == "POST":
		g.delete()
		return redirect('/notes')
	return render(request,'notedelete.html',{'b':g})







