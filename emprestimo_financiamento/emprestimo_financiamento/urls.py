from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from imoveis.views import ImovelViewSet, FinanciamentoViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register(r'imoveis', ImovelViewSet)
router.register(r'financiamentos', FinanciamentoViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="API de Empréstimos e Financiamentos de Imóveis",
        default_version='v1',
        description="API para gerenciar o empréstimo e financiamento de imóveis",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="suporte@empresa.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
