
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.generics import TemplateAPIView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^test/',TemplateAPIView.as_view('template_name=index.html'))
]
