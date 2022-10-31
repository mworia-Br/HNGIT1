from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task1-list/', views.task1List, name="task1-list"),
]