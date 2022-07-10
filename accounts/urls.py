from unicodedata import name
from django.urls import URLPattern, path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', views.logout, name="logout"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view())
]