from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include('api.v1.urls')),
]
