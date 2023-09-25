from django.urls import path
from .views import LikeListCreateView, LikeRetrieveView

urlpatterns = [
    path('<int:pk>/', LikeRetrieveView.as_view(), name='like-retrieve-destroy'),
    path('', LikeListCreateView.as_view(), name='like-list-create'),
]
