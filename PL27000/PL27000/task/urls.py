from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('list/', views.read_view),
    path('create/', views.create_view),
    path('delete/<pk>', views.delete_view),
    path('update/<pk>', views.update_view),
]
