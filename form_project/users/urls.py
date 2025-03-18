from django.urls import path
from .views import user_form, user_list

urlpatterns = [
    path('forms/', user_form, name = 'user_form'), # form page
    path('users/', user_list, name = 'user_list'), # display users/submissions
]