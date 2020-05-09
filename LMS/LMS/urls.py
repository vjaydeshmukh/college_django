from django.contrib import admin
from django.urls import path, include
from management import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(url)),
]
