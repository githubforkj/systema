from django.urls import path

from .views import  FormClass, ListClass #IndexView
from . import views

app_name = 'reload'
urlpatterns=[
        #path('', IndexView.as_view()),
        path('ajax-number/', views.ajax_number, name = 'ajax_number'),
        path('', views.index, name='index'),
        path('form/', FormClass.as_view(), name='form'),
        path('list/', ListClass.as_view(), name='list'),
        path('test/', views.test, name='test'),
        #path('static/map.html', AboutView.as_view()),
        #path('about/', AboutView.as_view()),
        #path('about/', views.about_page, name='about_page'),
]
