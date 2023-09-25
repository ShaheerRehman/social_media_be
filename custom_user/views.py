from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CustomUser
from .serializers import CustomUserSerializer, BuildingSerializer
from rest_framework import viewsets, status, generics
from rest_framework.authtoken.models import Token


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token, created = Token.objects.get_or_create(user=serializer.instance)
            data = serializer.data
            data['token'] = token.key

            # return Response({'token': token.key})
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            data = serializer.data
            data['id'] = user.id
            data['username'] = user.username
            data['email'] = user.email
            data['token'] = token.key

            # return Response({'token': token.key})
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBuildingView(generics.ListAPIView):
    serializer_class = BuildingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CustomUser.objects.filter(building_name__isnull=False).exclude(building_name=self.request.user.building_name)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.values('building_name').distinct()
        serializer = BuildingSerializer(queryset, many=True)
        return Response(serializer.data)
