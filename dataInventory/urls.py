from rest_framework import routers
from .api import ProductViewSet,EnterpriseViewSet,OrdenViewSet,ClienteViewSet,CategoriaViewSet
router= routers.DefaultRouter()

router.register('api/products',ProductViewSet,'products')
router.register('api/companies',EnterpriseViewSet,'enpterprises')
router.register('api/categories',CategoriaViewSet,'categorias')
router.register('api/customers',ClienteViewSet,'clientes')
router.register('api/orders',OrdenViewSet,'ordenes')
urlpatterns = router.urls

