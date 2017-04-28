from django.conf.urls import url
from .views import UserLoginAPIView, request_user, sold_summary_list, city_area_list, house_category_list, test
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^api/login/$', UserLoginAPIView.as_view()),
    url(r'^api/request_user/$', request_user),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api/sold_summary/', sold_summary_list),
    url(r'^api/city_area/', city_area_list),
    url(r'^api/house_category/', house_category_list),
    url(r'^api/test/', test),
]