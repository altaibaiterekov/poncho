from rest_framework.routers import SimpleRouter
from product.views import ProductViewSet#, ProductImageViewSet

router = SimpleRouter()
router.register('', ProductViewSet)
# router.register('images', ProductImageViewSet)


urlpatterns = []
urlpatterns += router.urls
