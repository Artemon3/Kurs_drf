import rest_framework
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.permissions import IsOwner
from habit.serializers import HabitSerializer


# Create your views here.
class HabitCreateAPIView(rest_framework.generics.CreateAPIView):
    """ Create lesson """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitListAPIView(rest_framework.generics.ListAPIView):
    """ All lesson """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitPaginator


class HabitRetrieveAPIView(rest_framework.generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(rest_framework.generics.UpdateAPIView):
    """ Update lesson """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDestroyAPIView(rest_framework.generics.DestroyAPIView):
    """ Delete lesson """
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PublicHabitListAPIView(rest_framework.generics.ListAPIView):
    """ All public lesson """
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_published=True)
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator
