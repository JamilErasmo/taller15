from django.urls import path, include, admin
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'edificios', views.EdificioViewSet)
router.register(r'propietarios', views.PropietarioViewSet)
router.register(r'departamentos', views.DepartamentoViewSet)

urlpatterns = [
path('admin/', admin.site.urls),
    #http://127.0.0.1:8000/api/edificios
    #http://127.0.0.1:8000/api/propietarios
    #http://127.0.0.1:8000/api/departamentos
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]