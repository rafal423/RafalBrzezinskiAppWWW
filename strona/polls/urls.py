from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('osoby/', views.person_list),
    path('osoby/<int:pk>/', views.person_detail),

]