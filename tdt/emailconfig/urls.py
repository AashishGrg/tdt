from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from emailconfig import views


app_name = 'emailconfig'
urlpatterns = [
	path('user/fetch/parent/',(views.FetchParentView.as_view()), name='fetchparent'),
	

	]
