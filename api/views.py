from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework_expiring_authtoken.authentication import ExpiringTokenAuthentication
#from .serializers import ArticleSerializer, CommentSerializer, TagSerializer
from rest_framework.decorators import api_view, authentication_classes
#from blog.models import Article, Comment, Tag
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import UserLoginSerializer, SoldSummarySerializer, HouseCategorySerializer, CityAreaSerializer, HouseForSaleSerializer, HouseSoldSerializer
from rest_framework.authtoken.models import Token
from rest_framework_expiring_authtoken.models import ExpiringToken
#from .paginator import get_page_list
from django.core.paginator import Paginator
import datetime
import requests
from django.conf import settings
from .models import SoldSummary, HouseCategory, CityArea, HouseForSale, HouseSold
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import json
import pandas as pd

'''
python manage.py shell
from api.models import *
'''
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

'''
solds = SoldSummary.objects.using('realtor').all()
solds = solds.filter(city__exact='Richmond Hill')
solds = solds.filter(area__exact='Langstaff')
solds = solds.filter(category__exact='t3')
mlist = solds.values()
df = pd.DataFrame(list(mlist))

kwargs = {
'{0}__{1}'.format('name', 'startswith'): 'A',
'{0}__{1}'.format('name', 'endswith'): 'Z'
}
'''
@api_view(['GET'])
@cache_page(3600)
def sold_summary_list(request, city, area, category):
    """
    List all SoldSummary
    http://127.0.0.1:8000/api/sold_summary/Richmond%20Hill/Langstaff/t3/
    """
    paras = {}

    if isBlank(city) and not isBlank(request.GET.get('city')):
        city = request.GET.get('city')
   
    if not isBlank(city):
        paras['city'] = city

    if isBlank(area) and not isBlank(request.GET.get('area')):
        area = request.GET.get('area')

    if not isBlank(area):
        paras['area'] = area

    if isBlank(category) and not isBlank(request.GET.get('category')):
        category = request.GET.get('category')
    
    if not isBlank(category):
        paras['category'] = category

    kwargs = {}

    for key,value in paras.items():
        kwargs['{0}__{1}'.format(key, 'exact')] = value

    solds = SoldSummary.objects.using('realtor').filter(**kwargs)
    '''
    solds = SoldSummary.objects.using('realtor').all()
    if not isBlank(city):
        solds = solds.filter(city__exact=city)
    if not isBlank(area):
        solds = solds.filter(area__exact=area)
    if not isBlank(category):
        solds = solds.filter(category__exact=category)
    '''
    '''
    paras = {}
    if not isBlank(city):
        paras['city'] = city
    if not isBlank(area):
        paras['area'] = area
    if not isBlank(category):
        paras['category'] = category
    

    f = ' and '.join(['%s = \'%s\'' % (key, value) for (key, value) in paras.items()])
    
    q = 'select * from vw_sum_sold where {0}'.format(f)

    hasFilter = not isBlank(city) or not isBlank(area) or not isBlank(category)
    if hasFilter:
        solds = SoldSummary.objects.using('realtor').raw(q)
    else:
        solds = SoldSummary.objects.using('realtor').all()
    '''
    serializer = SoldSummarySerializer(solds, many=True)
    # return Response(serializer.data, status=status.HTTP_200_OK)
    if not isBlank(paras.get('area')):
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def house_report(request):
    city = request.GET.get('city')
    area = request.GET.get('area')
    category = request.GET.get('category')
    df2 = pd.DataFrame({'key': ['city', 'area', 'category'],
                 'data2': [city,area,category]})
    return Response(df2.to_dict(orient='records'), status=status.HTTP_200_OK)

@api_view(['GET'])
@cache_page(3600)
def city_area_list(request):
    """
    List all CityArea
    """
    mlist = CityArea.objects.using('realtor').all()
    serializer = CityAreaSerializer(mlist, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@cache_page(3600)
def city_list(request):
    """
    List all City
    http://127.0.0.1:8000/api/city/
    """
    mlist = CityArea.objects.using('realtor').all().values()
    df = pd.DataFrame(list(mlist))
    df1 = df[['city']].drop_duplicates()
    # serializer = CityAreaSerializer(mlist, many=True)
    return Response(df1.to_dict(orient='records'), status=status.HTTP_200_OK)

def isBlank(myString):
    return not (myString and myString.strip())

@api_view(['GET'])
def area_list(request, city):
    """
    List all area
    http://127.0.0.1:8000/api/area/Richmond%20Hill/
    """
    mlist = CityArea.objects.using('realtor').all().values()
    df = pd.DataFrame(list(mlist))
    if not isBlank(city):
        df = df[df['city'] == city]
    df1 = df[['area']].drop_duplicates()
    # serializer = CityAreaSerializer(mlist, many=True)
    return Response(df1.to_dict(orient='records'), status=status.HTTP_200_OK)

@api_view(['GET'])
@cache_page(3600)
def house_category_list(request):
    """
    List all HouseCategory
    """
    mlist = HouseCategory.objects.using('realtor').all().values()
    df = pd.DataFrame(list(mlist))
    df1 = df[['name','en','cn']]
    # serializer = HouseCategorySerializer(mlist, many=True)
    # l = list(mlist)
    # t = type(serializer.data)
    # j = json.dumps(serializer.data)
    return Response(df1.to_dict(orient='records'), status=status.HTTP_200_OK)

LongitudeMin = -128.02981853485105
LongitudeMax = -60.67631874511719
LatitudeMin = 20.9452976572409
LatitudeMax = 60.3041267770092

@api_view(['GET'])
def house_for_sale_list(request):
    """
    List all HouseForSale
    43.78760887990924,43.81238855081077,-79.4278062438965,-79.33210502624513
    http://127.0.0.1:8000/api/house_for_sale/?from=20170401&to=20170501&latitude1=43.78760887990924&latitude2=43.81238855081077&longitude1=-79.4278062438965&longitude2=-79.33210502624513
    """
    latitude1 = LatitudeMin
    if not isBlank(request.GET.get('latitude1')):
        latitude1 = request.GET.get('latitude1')

    latitude2 = LatitudeMax
    if not isBlank(request.GET.get('latitude2')):
        latitude2 = request.GET.get('latitude2')

    longitude1 = LongitudeMin
    if not isBlank(request.GET.get('longitude1')):
        longitude1 = request.GET.get('longitude1')

    longitude2 = LongitudeMax
    if not isBlank(request.GET.get('longitude2')):
        longitude2 = request.GET.get('longitude2')

    solds = HouseForSale.objects.using('realtor').all()

    solds = solds.filter(latitude__gt=latitude1)   
    solds = solds.filter(latitude__lt=latitude2)   
    solds = solds.filter(longitude__gt=longitude1)   
    solds = solds.filter(longitude__lt=longitude2)   

    if not isBlank(request.GET.get('from')):
        from_str = request.GET.get('from')
        from_date = datetime.datetime.strptime(from_str, "%Y%m%d")
        solds = solds.filter(inputdate__gte=from_date)

    if not isBlank(request.GET.get('to')):
        to_str = request.GET.get('to')
        to_date = datetime.datetime.strptime(to_str, "%Y%m%d")
        solds = solds.filter(inputdate__lte=to_date)

    serializer = HouseForSaleSerializer(solds, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    #return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def house_sold_list(request):
    """
    import datetime
    parsed_date = datetime.datetime.strptime('20170611', "%Y%m%d")
    List all HouseSold
    http://127.0.0.1:8000/api/house_sold/?latitude1=43.78760887990924&latitude2=43.81238855081077&longitude1=-79.4278062438965&longitude2=-79.33210502624513
    http://127.0.0.1:8000/api/house_sold/?from=20170401&to=20170501&latitude1=43.78760887990924&latitude2=43.81238855081077&longitude1=-79.4278062438965&longitude2=-79.33210502624513
    """
    latitude1 = LatitudeMin
    if not isBlank(request.GET.get('latitude1')):
        latitude1 = request.GET.get('latitude1')

    latitude2 = LatitudeMax
    if not isBlank(request.GET.get('latitude2')):
        latitude2 = request.GET.get('latitude2')

    longitude1 = LongitudeMin
    if not isBlank(request.GET.get('longitude1')):
        longitude1 = request.GET.get('longitude1')

    longitude2 = LongitudeMax
    if not isBlank(request.GET.get('longitude2')):
        longitude2 = request.GET.get('longitude2')

    solds = HouseSold.objects.using('realtor').all()

    solds = solds.filter(latitude__gt=latitude1)   
    solds = solds.filter(latitude__lt=latitude2)   
    solds = solds.filter(longitude__gt=longitude1)   
    solds = solds.filter(longitude__lt=longitude2)   

    if not isBlank(request.GET.get('from')):
        from_str = request.GET.get('from')
        from_date = datetime.datetime.strptime(from_str, "%Y%m%d")
        solds = solds.filter(solddate__gte=from_date)

    if not isBlank(request.GET.get('to')):
        to_str = request.GET.get('to')
        to_date = datetime.datetime.strptime(to_str, "%Y%m%d")
        solds = solds.filter(solddate__lte=to_date)
          
    serializer = HouseSoldSerializer(solds, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    #return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def test(request):
    """
    List all test commit test
    """
    mlist = HouseCategory.objects.using('realtor').all().values()
    df = pd.DataFrame(list(mlist))
    df1 = df[['name','en','cn']]
    # serializer = HouseCategorySerializer(mlist, many=True)
    # l = list(mlist)
    # t = type(serializer.data)
    # j = json.dumps(serializer.data)
    return Response(df1.to_dict(orient='records'), status=status.HTTP_200_OK)