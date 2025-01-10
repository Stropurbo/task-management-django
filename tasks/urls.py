from django.urls import path
from tasks.views import show_task, show_dynamic_task

urlpatterns = [
    path('show_task/', show_task),
    path('show_task/<int:id>/', show_dynamic_task),
    
]