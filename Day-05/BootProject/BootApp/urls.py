from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name="hm"),
	path('about/',views.about,name="ab"),
	path('contact/',views.contact,name="ct"),
	path('notes/',views.noteall,name="nt"),
	path('ednt/<int:h>/',views.noteup,name="ntup"),
	path('edj/<int:p>/',views.notedlt,name="ntdl"),
]