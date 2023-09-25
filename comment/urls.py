from django.urls import path
from .views import CommentListCreateView, CommentRetrieveUpdateDestroyView

urlpatterns = [
    path('', CommentListCreateView.as_view(), name='comment-list-create'),
    path('<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-retrieve-update-destroy'),
]
