from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',v.product, name='products.html'),
]