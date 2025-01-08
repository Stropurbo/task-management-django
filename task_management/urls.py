from django.contrib import admin
from django.urls import path, include
from tasks.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('users/', include('users.urls')),
    path('tasks/', include('tasks.urls')),
]
