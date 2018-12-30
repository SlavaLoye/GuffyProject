from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # динамически меняем название страницы ab/
    path('about/', views.AboutPageView.as_view(), name='about'),
]




