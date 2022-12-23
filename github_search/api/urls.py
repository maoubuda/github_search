from rest_framework.routers import DefaultRouter
from api.views import ReposViewSet


app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'repos', ReposViewSet)

urlpatterns = router.urls
