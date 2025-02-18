from django.urls import path
from tasks.views import dashboard, user_dashboard, test, create_task,view_task

urlpatterns = [
    path('dashboard/', dashboard),
    path('user_dashboard/', user_dashboard),
    path('test/', test),
    path('create_task', create_task),
    path('view_task', view_task)

    
]