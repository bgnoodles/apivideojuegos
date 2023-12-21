from rest_framework import routers
from .api import VideojuegoViewset

router = routers.DefaultRouter()
router.register('api/videojuegos', VideojuegoViewset, 'videojuegos')

urlpatterns = router.urls