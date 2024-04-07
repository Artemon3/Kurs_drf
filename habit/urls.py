from django.urls import path

from habit.views import HabitCreateAPIView, HabitListAPIView, HabitUpdateAPIView, HabitDestroyAPIView, \
    HabitRetrieveAPIView, PublicHabitListAPIView

from habit.apps import HabitConfig

app_name = HabitConfig.name


urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('habit/', HabitListAPIView.as_view(), name='habit-list'),
    path('habit/', HabitRetrieveAPIView.as_view(), name='habit-get'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),
    path('public_habit/', PublicHabitListAPIView.as_view(), name='public-habit-list'),
]
