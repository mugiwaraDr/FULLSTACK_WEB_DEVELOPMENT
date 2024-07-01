from django.contrib import admin
from django.urls import path
from ap2.views import showlist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('showlist/', showlist),
]
