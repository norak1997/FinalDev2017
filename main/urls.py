from django.conf.urls import url
from . import views

app_name='main'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add/$',views.add, name='add'),#done
   	url(r'^disp/$',views.disp, name='disp'),
   	url(r'^wrong/$',views.wrong, name='wrong'),	
]
