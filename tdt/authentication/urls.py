from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from authentication import views


app_name = 'authentication'
urlpatterns = [
	# path('signup/',(views.UserSignupForm.as_view()), name='signup'),
	path('admin/signup/',(views.AdminUserSignupForm.as_view()), name='admin_signup'),
	path('user/signup/',(views.NormalUserSignupForm.as_view()), name='user_signup'),
	path('logout/', views.logout_view, name='logout'),
	path('login/', (auth_views.LoginView.as_view(template_name='index.html')), name='login'),
	]
