from django.urls import path
from . import views

urlpatterns =[
#path(r'(?P<pk>\d+)/$', views.index, name='index'),
    path('index', views.index, name='index'),
    path("new", views.new)

]