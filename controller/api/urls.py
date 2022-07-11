from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('request/<int:request_id>/', views.request, name='request'),
        path('response/<int:request_id>/', views.response, name='response'),
        path('did', views.createDID, name='createDID'),
]
