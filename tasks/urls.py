from django.urls import path
from tasks.views import dashboard, user_dashboard, test

urlpatterns = [
    path('dashboard/', dashboard),
    path('user_dashboard/', user_dashboard),
    path('test/', test),

    
]