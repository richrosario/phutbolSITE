from django.urls import path
from . import views #grab home function in views

urlpatterns = [
    path('', views.home, name = 'liveScore-home'),
    path('about/', views.about, name = 'liveScore-about')
]

#here we map urls that correspond to each view function 