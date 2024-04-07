from rest_framework.serializers import ValidationError


class RelateAndRewardValidator:

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)

        if not related_habit or not reward:
            return
        raise (ValidationError
               ('Нельзя использовать одновременно '
                'связанную привычку и вознаграждение'))


class HabitRelatedHabitIsPleasantValidator:

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        is_pleasant = dict(value).get(self.field2)

        if not related_habit or is_pleasant:
            return
        raise (ValidationError
               ('Связанной привычкой может быть только приятная привычка'))


class HabitPleasantValidator:

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)
        is_pleasant = dict(value).get(self.field3)

        if not is_pleasant or not reward or not related_habit:
            return
        raise (ValidationError
               ("У приятной привычки не может быть вознаграждения "
                "или связанной привычки"))


class HabitTimeDurationValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_on_action = dict(value).get(self.field)

        if not time_on_action or time_on_action <= 120:
            return
        raise (ValidationError
               ('Выполнение привычки не может превышать 120 секунд'))


class CheckHabitValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        period = dict(value).get(self.field)

        if not isinstance(period, int) or period <= 7 and period >= 1:
            return
        raise (ValidationError
               ('Периодичность привычки не может быть больше 7 и меньше 1'))
