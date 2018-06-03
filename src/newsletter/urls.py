from django.urls import path 
from .views  import  newsletter_subscribe
app_name = 'newsletter'
urlpatterns = [
        path('subscribe', newsletter_subscribe, name='subscribe'),
     ]