from .models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'building_name', 'apartment_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.building_name = validated_data.get('building_name', instance.building_name)
        instance.apartment_number = validated_data.get('apartment_number', instance.apartment_number)
        instance.email = validated_data.get('email', instance.email)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance

    def validate(self, data):
        if not data['apartment_number'] or not data['building_name']:
            raise serializers.ValidationError("apartment number and building name must be filled")
        if data['apartment_number'] < 0:
            raise serializers.ValidationError("apartment number must be positive")
        return data


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['building_name']

