from django.urls import path
from . import views
from django.contrib.auth import views as dy

urlpatterns = [
	path('',views.home,name="hm"),
	path('rg/',views.register,name="reg"),
	path('login/',dy.LoginView.as_view(template_name='html/login.html'),name="lg"),
	path('logout/',dy.LogoutView.as_view(template_name='html/logout.html'),name="lgo"),
]