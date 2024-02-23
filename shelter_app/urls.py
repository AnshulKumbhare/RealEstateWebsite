from django.contrib import admin
from django.urls import path
from shelter_app import views
from shelter import settings
from django.conf.urls.static import static

urlpatterns = [
    path('header', views.header),
    path('footer', views.footer),
    path('register', views.register),
    path('login', views.user_login),
    path('logout', views.user_logout),
    path('home', views.home),
    path('about', views.about),
    path('contact', views.contactus),
    path('agents', views.agents),
    path('shelterproperty', views.shelterproperty),
    path('buyproperty', views.buyproperty),
    path('rentproperty', views.rentproperty),
    path('shelterpropertytype/<type>', views.shelterpropertytype),
    path('sortbeds/<bed>', views.sortbeds),
    path('sortarea/<alimit>', views.sortarea),
    path('sortareabelow/<alimit>', views.sortareabelow),
    path('sortareaabove/<alimit>', views.sortareaabove),
    path('plimitbelow/<pl>', views.plimitbelow),
    path('booked', views.booked),
    path('booking/<pid>', views.booking),
    path('removebooking/<bid>', views.removebooking),
    path('submitproperty', views.submitproperty),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)