from .views import index, success
from django.urls import path



app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('success', success, name='success'),

]