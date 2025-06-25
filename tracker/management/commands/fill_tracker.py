from django.core.management.base import BaseCommand
from faker import Faker
import pandas as pd
import random

class Command(BaseCommand):
    help = 'Генерирует случайные задачи и сохраняет их в CSV'

    def handle(self, *args, **kwargs):
        fake = Faker()
        num_records = 100
        statuses = ['Не активна', 'В работе', 'Выполнена']

        data = {
            'ID задачи': [],
            'Название': [],
            'Связанная приятная задача': [],
            'Статус выполнения': [],
            'Срок выполнения': [],
            'Сотрудники': [],
            'Дата создания': [],
        }

        for task_id in range(1, num_records + 1):
            data['ID задачи'].append(task_id)
            data['Название'].append(fake.sentence(nb_words=6))
            data['Связанная приятная задача'].append(fake.text(max_nb_chars=200))
            data['Статус выполнения'].append(random.choice(statuses))
            data['Срок выполнения'].append(str(fake.date_between(start_date='today', end_date='+30d')))
            data['Сотрудники'].append(fake.name())
            data['Дата создания'].append(str(fake.date_this_year()))

        df = pd.DataFrame(data)
        df.to_csv('task_tracker.csv', index=False, encoding='utf-8-sig')

        self.stdout.write(self.style.SUCCESS("Таблица задач успешно заполнена и сохранена в 'task_tracker.csv'"))