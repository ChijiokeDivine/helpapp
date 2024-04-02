from .views import index, success, waitlist
from django.urls import path



app_name = 'core'

urlpatterns = [
    path('help/secret-url/', index, name="index"),
    path('', waitlist, name='waitlist'),
    path('success/', success, name='success'),

]