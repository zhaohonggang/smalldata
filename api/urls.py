from django.conf.urls import url, include
from .views import UserLoginAPIView, request_user, sold_summary_list, city_area_list, city_list, area_list, house_category_list, house_for_sale_list, house_sold_list, house_report, test
from rest_framework.authtoken import views
from django.views.generic.base import RedirectView, TemplateView

urlpatterns = [
    url(r'^api/login/$', UserLoginAPIView.as_view()),
    url(r'^api/request_user/$', request_user),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api/sold_summary/((?P<city>[\w\s\.-]+)/)?((?P<area>[^/\n]+)/)?((?P<category>[\w\s\.-]+)/)?', sold_summary_list),
    url(r'^api/city_area/', city_area_list),
    url(r'^api/city/', city_list),
    url(r'^api/area/((?P<city>[\w\s\.-]+)/)?', area_list),
    url(r'^api/house_category/', house_category_list),
    url(r'^api/house_for_sale/', house_for_sale_list),
    url(r'^api/house_sold/', house_sold_list),
    url(r'^api/house_report/', house_report),
    url(r'^api/test/', test),
    url(r'^api/docs/', include('rest_framework_docs.urls')),
    #url(r'^api/$', include('rest_framework_docs.urls')),
    url(r'^api/$', RedirectView.as_view(url='/api/docs')),
]