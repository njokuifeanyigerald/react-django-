from django.urls import path, re_path
from .views import getRoutes, getNote, getNotes

# YASG

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Django-React",
      default_version='v1',
      description="Test description",
    #   can be configured
      terms_of_service="https://www.app.com/policies/terms/",
      contact=openapi.Contact(email="contact@expenses.local"),
    #   can be configured
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('',getRoutes, name='getRoutes' ),
    path('notes/', getNotes, name='getnotes'),
    path('note/<str:pk>/', getNote, name='getnote'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]
