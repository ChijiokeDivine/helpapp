from .views import index, success, waitlist
from django.urls import path



app_name = 'core'

urlpatterns = [
    path('', index, name="index"),
    path('waitlist/', waitlist, name='waitlist'),
    path('success/', success, name='success'),

]