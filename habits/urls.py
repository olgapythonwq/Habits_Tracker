from rest_framework.routers import DefaultRouter
from .views import HabitViewSet, PublicHabitViewSet

router = DefaultRouter()
router.register(r"habits/public", PublicHabitViewSet, basename="public-habit")
router.register(r"habits", HabitViewSet, basename="habit")

urlpatterns = router.urls
