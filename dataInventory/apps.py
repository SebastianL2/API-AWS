from django.apps import AppConfig


class DatainventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dataInventory'

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

class EmpresaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'enterprise'

class CategoriaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'categorias'

class ClienteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientes'


class OrdenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ordenes'


class EmpresaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'