from datetime import datetime, date, timedelta

import requests
from celery import shared_task
from django.conf import settings

from habit.models import Habit


@shared_task
def send_reminder_about_habit():
    """
    Отправка пользователю в Телеграм напоминания о привычке
    """
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_TOKEN

    time_now = datetime.now().time().replace(second=0, microsecond=0)
    date_now = date.today()
    habit_to_send = Habit.objects.filter(nice_habit_bool=False)

    for habit in habit_to_send:
        if habit.date == date_now or not habit.date:
            if habit.time >= time_now:
                chat_id = habit.owner.telegram_id
                text = f"Вам нужно {habit.action} в {habit.time} в {habit.place}"
                requests.post(
                    url=f"{URL}{TOKEN}/sendMessage",
                    data={
                        "chat_id": chat_id,
                        "text": text
                    }
                )
            habit.date = date_now + timedelta(days=habit.period)
            habit.save()
