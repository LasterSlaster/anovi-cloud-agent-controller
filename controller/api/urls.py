from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
        path('', views.index, name='index'),
        path('request/<int:request_id>/', views.request, name='request'),
        path('response/<int:request_id>/', views.response, name='response'),
        path('did', views.createDID, name='createDID'),
]
