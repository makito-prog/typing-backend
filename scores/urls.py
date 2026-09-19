from django.urls import path
from . import views

urlpatterns = [
    path('scores/', views.ScoreListCreateView.as_view(), name='score-list'),
]