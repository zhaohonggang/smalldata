from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework_expiring_authtoken.authentication import ExpiringTokenAuthentication
#from .serializers import ArticleSerializer, CommentSerializer, TagSerializer
from rest_framework.decorators import api_view, authentication_classes
#from blog.models import Article, Comment, Tag
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import UserLoginSerializer, SoldSummarySerializer, HouseCategorySerializer, CityAreaSerializer
from rest_framework.authtoken.models import Token
from rest_framework_expiring_authtoken.models import ExpiringToken
#from .paginator import get_page_list
from django.core.paginator import Paginator
import datetime
import requests
from django.conf import settings
from .models import SoldSummary, HouseCategory, CityArea
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import json
import pandas as pd

# Create your views here.
class UserLoginAPIView(APIView):
    permission_classes = []
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        username = request.data.get('username')
        password = request.data.get('password')
        serializer = self.serializer_class(data=data)
        try:
            if serializer.is_valid(raise_exception=True):
                user = serializer.validated_data['user']
                token, created = ExpiringToken.objects.get_or_create(user=user)
                response = Response('Setting a cookie')
                #response.set_cookie('cookie', 'MY COOKIE VALUE')
                response.set_cookie('Token', token.key)
                if not created:
                    token.created = datetime.datetime.utcnow()
                    token.save()
                return Response({'token': token.key,'url':''}, status=status.HTTP_200_OK)
        except:
            LOGIN_SITES = getattr(settings, "LOGIN_SITES", None)
            for key, value in LOGIN_SITES.items():
                r = requests.post(key, data = {'username':username,'password':password,'url':''})
                if r.json()['Msg'] == 'Success':
                    return Response({'token': r.json()['Token'],'url':value.format(r.json()['Token'])}, status=status.HTTP_200_OK)
            return Response({'error'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes((ExpiringTokenAuthentication,))
def request_user(request):
    print(request.auth)
    if request.auth:
        user_info = request.user
        token = ExpiringToken.objects.first()
        token.created = datetime.datetime.utcnow()
        token.save()
        return Response({'user': str(user_info)}, status=status.HTTP_200_OK)
    else:
        return Response({'user': 'not_login'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@cache_page(3600)
def sold_summary_list(request):
    """
    List all SoldSummary
    """
    solds = SoldSummary.objects.using('realtor').all()
    serializer = SoldSummarySerializer(solds, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@cache_page(3600)
def city_area_list(request):
    """
    List all CityArea
    """
    mlist = CityArea.objects.using('realtor').all()
    serializer = CityAreaSerializer(mlist, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@cache_page(3600)
def house_category_list(request):
    """
    List all HouseCategory
    """
    mlist = HouseCategory.objects.using('realtor').all()
    serializer = HouseCategorySerializer(mlist, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def test(request):
    """
    List all test
    """
    mlist = HouseCategory.objects.using('realtor').all().values()
    # serializer = HouseCategorySerializer(mlist, many=True)
    # l = list(mlist)
    # t = type(serializer.data)
    # j = json.dumps(serializer.data)
    return Response(mlist, status=status.HTTP_200_OK)