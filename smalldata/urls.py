"""smalldata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    python manage.py shell
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from businessadmin.admin import admin_site
from django.views.generic.base import RedirectView, TemplateView
from frontend import views as frontend_views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', admin_site.urls),
    url(r'^', include('api.urls')),
    # url(r'^$', RedirectView.as_view(url='/admin')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    # url(r'^history/$', TemplateView.as_view(template_name='history.html')),
    # url(r'^history1/$', frontend_views.history, name='history1'),
    # url(r'^his/$', frontend_views.his, name='his'),
    url(r'^(?P<foldername>housing|house)/((?P<filename>[\w]+)/)?', frontend_views.bag, name='housing'),
    url('^payments/', include('payments.urls')),
    # url(r'^map/$', TemplateView.as_view(template_name='map.html')),
]

