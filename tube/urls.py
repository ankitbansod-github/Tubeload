from django.urls import path
from . import views

app_name='tube'

urlpatterns=[
    path('',views.index ,name='index'),
    path('process/',views.process,name='process'),
    path('result/<res>',views.result,name='result'),
    path('about/',views.about,name='about'),
    path('help/',views.help,name='help'),
]