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




