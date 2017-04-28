from rest_framework import serializers
#from blog.models import Article, Tag, Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from .models import SoldSummary, HouseCategory, CityArea

class DateTimeFieldWihTZ(serializers.DateTimeField):

    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeFieldWihTZ, self).to_representation(value)

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        if not user or not username:
            raise serializers.ValidationError({'login_err': 'Username or password is wrong!'})
        attrs['user'] = user
        return attrs

class SoldSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldSummary
        fields = '__all__'

class HouseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseCategory
        exclude = ('id',)

class CityAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityArea
        exclude = ('id',)