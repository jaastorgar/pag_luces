from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, arriendo

urlpatterns = [
    path('', home, name="home"),
    path('arriendo/', arriendo, name="arriendo"),
]