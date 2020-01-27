
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls import url
from adminhome.views import home,managecourse,course,courseupload,login



urlpatterns = [

	# path('login/',TemplateView.as_view(template_name='login.html'),name='login_page'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('header/',TemplateView.as_view(template_name='header.html'),name='header'),
    url('base/',TemplateView.as_view(template_name='base.html'), name='base'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
    url(r'^home/$',home,name='home_page'),
    url(r'^managecourse/$',managecourse,name='managecourse'),
    url(r'^course/$',course,name='course'),
	url(r'^courseupload/$',courseupload,name='courseupload'),
	url(r'^login/$',login,name='login'),


]