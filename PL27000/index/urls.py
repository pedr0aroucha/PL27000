from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
	path('', views.index_view),
	path('login/', views.login_view),
	path('logout/', views.logout_view),
	path('register/', views.register_view),
	path('help/', views.help_view)
]