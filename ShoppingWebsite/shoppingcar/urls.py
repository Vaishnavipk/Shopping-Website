from django.urls import path
from shoppingcar import views


app_name = 'shoppingcar'
urlpatterns = [
    path('', views.shoppingcar, name='shoppingcar'),
]