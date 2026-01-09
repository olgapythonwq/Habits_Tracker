from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Habit
from .pagination import HabitPagination
from .permissions import IsOwner
from .serializers import HabitSerializer


class HabitViewSet(ModelViewSet):
    # queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitPagination

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PublicHabitViewSet(ReadOnlyModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)
