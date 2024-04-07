from rest_framework import serializers

from habit.models import Habit
from habit.validators import (RelateAndRewardValidator, HabitRelatedHabitIsPleasantValidator, HabitPleasantValidator,
                               CheckHabitValidator, HabitTimeDurationValidator)


class HabitSerializer(serializers.ModelSerializer):
    """ Сериалайзер для модели Habit """
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelateAndRewardValidator(field1='nice_habit', field2='reward'),
            HabitRelatedHabitIsPleasantValidator(field1='nice_habit', field2='nice_habit_bool'),
            HabitPleasantValidator(field1='nice_habit', field2='reward', field3='nice_habit_bool'),
            HabitTimeDurationValidator(field='time_on_action'),
            CheckHabitValidator(field='period')
        ]