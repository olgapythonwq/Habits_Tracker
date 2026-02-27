from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Habit
from .pagination import HabitPagination
from .permissions import IsOwner
from .serializers import HabitSerializer
from drf_spectacular.utils import extend_schema


class HabitViewSet(ModelViewSet):
    # queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitPagination

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@extend_schema(
    summary="Public habits list",
    description="Returns list of public habits available for all users",
)
class PublicHabitViewSet(ReadOnlyModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)
