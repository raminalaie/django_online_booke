from django.urls import *
from . import views
urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup")
]
