from django.urls import path
from django.views.generic.base import TemplateView
from . import views
app_name = "owner"

urlpatterns = [
    path('register/',views.register_owner, name="register"),
    path('thanks/',
         TemplateView.as_view(
             template_name="owner/registration_complete.html"),
         name="registration-complete"),

]


