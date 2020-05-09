from .views import *
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('', home, name='user_login'),
    path('dashboard/', dash, name='user_dashboard'),
    path('signout/', user_logout, name='user_log_out'),
    url(r'^borrow/(?P<b_id>[\w]+)/$', borrowit, name='user_borrow'),
    url(r'^return/(?P<b_id>[\w]+)/$', returnit, name='user_return'),
]