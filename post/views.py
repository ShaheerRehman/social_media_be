from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        building_name = self.request.query_params.get('building_name')
        author = self.request.query_params.get('author')
        apartment_number = self.request.query_params.get('apartment_number')
        queryset = Post.objects.all().order_by('-created_at')
        if building_name == "mine":
            building_name = self.request.user.building_name

        if building_name is not None and building_name != "mine":
            queryset = queryset.filter(user__building_name=building_name)

        if author is not None:
            queryset = queryset.filter(user__username=author)

        if apartment_number is not None:
            queryset = queryset.filter(user__apartment_number=apartment_number)

        return queryset

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

