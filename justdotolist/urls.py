from . import views
from django.urls import path


urlpatterns = [
    path('', views.BlogPost.as_view(), name='home'),
    path('register/', views.register, name='register'),
]
