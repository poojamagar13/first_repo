from django.contrib import admin
from django.urls import path , include
from vendor import views
#from django.conf.urls import url

urlpatterns =[
    path("contact", views.contact, name='contact'),
    path("retrieve", views.retrieve, name='retrieve'),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path(r'^delete_product/(?p<pk>[0-9]+)/$', views.delete , name="delete"),
    path("api1", views . FirstCRV  , view())

]