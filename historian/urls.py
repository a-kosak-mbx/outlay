from django.urls import path

from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('tags/', views.TagListView.as_view(), name='tags'),
]
