from rest_framework import routers
from .api import ProductViewSet,EnterpriseViewSet,OrdenViewSet,ClienteViewSet,CategoriaViewSet
router= routers.DefaultRouter()

router.register('api/products',ProductViewSet,'products')
router.register('api/Empresas',EnterpriseViewSet,'enpterprises')
router.register('api/Categorias',CategoriaViewSet,'categorias')
router.register('api/Clientes',ClienteViewSet,'clientes')
router.register('api/Ordenes',OrdenViewSet,'ordenes')
urlpatterns = router.urls

