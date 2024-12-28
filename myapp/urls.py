from django.urls import path
from myapp.views import index
urlpatterns = [
    path('<str:group_name>/', index),
]
