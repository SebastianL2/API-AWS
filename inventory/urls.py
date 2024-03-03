from rest_framework import routers
from .api import ProductViewSet
router= routers.DefaultRouter()

router.register('api/products',ProductViewSet,'products')
router.register('api/enterprises',ProductViewSet,'enpterprises')
