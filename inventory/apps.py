from django.apps import AppConfig


class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

class EnterpriseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'enterprises'

class EnterpriseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'