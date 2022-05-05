from django.urls import path

from . import views
from .views import *
from .views import EmailAttachementView
from django.urls import path


from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = (
    path('', index, name="index"),
    path('registration/', registration, name='register'),
    path("deathNote/", views.deathNote, name="deathNote"),
    path("aboutMe/", views.aboutMe, name="aboutMe"),
    path("home/", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("gallery/", views.gallery, name="gallery"),
    path("demonSlashingBlade/", views.demonSlashingBlade, name="demonSlashingBlade"),

    path('sends/', EmailAttachementView.as_view(), name='emailattachment'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
)
