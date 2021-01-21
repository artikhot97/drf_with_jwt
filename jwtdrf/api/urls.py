from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet,PaginationView,RegisterView
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

"""
Users will provide the list of all User of data
"""
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

"""
Swagger for API endpoint Documentaion
"""
schema_view = get_swagger_view(title="Swagger Docs")

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^users/register/$', RegisterView.as_view(), name='user-register'),
    url(r'^docs/', schema_view),
    url(r'^pagination_list/$',PaginationView.as_view()),
]