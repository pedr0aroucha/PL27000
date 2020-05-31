from django.contrib import admin
from django.urls import path, include
import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('PL27000.task.urls')),
    path('', include('index.urls')),
]
