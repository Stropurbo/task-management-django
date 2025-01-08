from django.urls import path
from users.views import user_contact,user_profile

urlpatterns = [
    path('user_contact/', user_contact),
    path('user_profile/', user_profile),
]