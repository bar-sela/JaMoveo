from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
   path("", views.signup , name = "signUp"),
   path("login", LoginView.as_view(), name='sign_in'),
   path("mainPage",views.mainPage, name='home'),
   path("search_songs", views.retrieve_songs, name ="search_songs"),
]