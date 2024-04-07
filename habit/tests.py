from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email="artemon3@test.ru",
            is_staff=True,
            is_active=True,
            is_superuser=False
        )
        self.user.set_password('1234')
        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            place='place',
            action='action',
            owner=self.user
        )

    def test_create_habit(self):
        """Тестирование создания привычек"""

        data = {
            'place': 'test_place',
            'time': '11:50:00',
            'action': 'test_action',
            'period': self.habit.period,
            'is_published': self.habit.is_published,
            'owner': self.user.pk,
        }

        response = self.client.post('/habit/create/', data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Habit.objects.all().count(), 2)

    def test_list_habit(self):
        """Тестирование вывода списка привычек"""

        response = self.client.get('/habit/')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': self.habit.id,
                            'date': self.habit.date,
                            'place': 'place',
                            'time': self.habit.time,
                            'action': 'action',
                            'nice_habit_bool': self.habit.nice_habit_bool,
                            'reward': self.habit.reward,
                            'time_on_action': self.habit.time_on_action,
                            'period': self.habit.period,
                            'is_published': self.habit.is_published,
                            'owner': self.user.pk,
                            'nice_habit': self.habit.nice_habit
                        }
                    ]
            }
        )

    def test_update_habit(self):
        """Тестирование изменения привычки"""

        change_data = {
            'place': 'place1',
            'action': 'action1'
        }
        response = self.client.patch(f'/habit/update/{self.habit.id}/', data=change_data)
        self.maxDiff = None

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(),
            {
                'id': self.habit.id,
                'date': self.habit.date,
                'place': 'place1',
                'time': self.habit.time,
                'action': 'action1',
                'nice_habit_bool': self.habit.nice_habit_bool,
                'reward': self.habit.reward,
                'time_on_action': self.habit.time_on_action,
                'period': self.habit.period,
                'is_published': self.habit.is_published,
                'owner': self.user.pk,
                'nice_habit': self.habit.nice_habit
            }
        )

    #
    def test_duration_habit(self):
        """Тестирование создания привычки со временем исполнения более 2 минут"""

        data = {
            'place': 'test_place',
            'action': 'test_action',
            'time_on_action': '130',
            'owner': self.user.pk,
        }
        response = self.client.post('/habit/create/', data=data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_periodicity_habit(self):
        """Тестирование создания привычки с периодичностью менее одного раза в неделю"""

        data = {
            'place': 'test_place',
            'action': 'test_action',
            'period': 8,
            'owner': self.user.pk
        }
        response = self.client.post('/habit/create/', data=data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_reward_and_pleasant_habit(self):
        """Тестирование создания привычки с наградой и приятной привычкой одновременно"""

        data = {
            'place': 'test_place',
            'action': 'test_action',
            'reward': 'reward_test',
            'owner': self.user.pk,
            'nice_habit': 1
        }
        response = self.client.post('/habit/create/', data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
