from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.php', views.index, name='index'),
    path('about.php', views.about, name='about'),
    path('contact.php', views.contact, name='contact'),
    path('users.php', views.users, name='users'),
]
