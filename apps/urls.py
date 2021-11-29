from django.urls import path
from . import views
urlpatterns=[
    path('apps/',views.dmfn,name='apps'),
    path('sample/',views.fnsample,name='sample')
] 