from django.db import models

from config import settings

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец привычки', **NULLABLE)
    place = models.CharField(max_length=50, verbose_name='Место')
    time = models.TimeField(default='10:00:00', verbose_name='Время')
    date = models.DateField(verbose_name='дата', **NULLABLE)
    action = models.CharField(max_length=200, verbose_name='Действие', **NULLABLE)
    nice_habit_bool = models.BooleanField(default=False, verbose_name='Признак полезной привычки')
    nice_habit = models.ForeignKey('self', on_delete=models.SET_NULL, max_length=100, verbose_name='Связанная привычка', **NULLABLE)
    period = models.IntegerField(default=1, verbose_name='периодичность', **NULLABLE)
    reward = models.CharField(max_length=100, verbose_name='Вознаграждение', **NULLABLE)
    time_on_action = models.TimeField(verbose_name='Время на выполнение', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='Признак публикации')

    def __str__(self):
        return f'{self.owner} будет {self.action} в {self.time} в/на {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
