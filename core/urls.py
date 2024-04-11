from .views import index, success, waitlist, contact, about, team,blog_detail
from django.urls import path



app_name = 'core'

urlpatterns = [
    path('help/secret-url/', index, name="index"),
    path('', waitlist, name='waitlist'),
    path('success/', success, name='success'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('our-team/', team, name='team'),
    path('blog/', blog_detail, name='blog-detail' )

]