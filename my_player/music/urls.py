from . import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('music/lyrics/<int:id>',views.lyr)
]