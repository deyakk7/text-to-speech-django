from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('list/', views.SoundList.as_view(), name='list'),
    path('list/<slug:slug>/', views.SoundDetail.as_view(), name='detail'),
]
