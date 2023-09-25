from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Like
from .serializers import LikeSerializer
from rest_framework.permissions import IsAuthenticated


class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeRetrieveView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            likes = Like.objects.filter(post_id=pk)
        except Like.DoesNotExist:
            return Response({"detail": "Like not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            like = Like.objects.get(id=pk)
        except Like.DoesNotExist:
            return Response({"detail": "Like not found."}, status=status.HTTP_404_NOT_FOUND)

        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

