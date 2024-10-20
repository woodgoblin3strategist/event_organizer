from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200) #название
    project = models.ForeignKey('Project', related_name='events', on_delete=models.SET_NULL, null=True, blank=True) #Проект - выбор из существующих
    subgroup = models.CharField(max_length=100) # Подгруппа - ввод текста
    event_type = models.CharField(max_length=50) # О событие
    is_owl_mode = models.BooleanField(default=False) # Режим сова
    start_date = models.DateTimeField() # Дата начала
    end_date = models.DateTimeField() # Дата окончания
    repetition = models.DateField() # Повтор события
    payment = models.DateField() # Оплата - число
    address = models.TextField(blank=True) # Адрес - ввод текста
    is_open = models.BooleanField(default=False) # Сделать событие открытым - чекбокс.
    comment = models.TextField(blank=True) # Комментарий - ввод текста.
    personal_note = models.TextField(blank=True) # Личная заметка - ввод текста
    organizers = models.ManyToManyField(User, related_name='event_organizers', blank=True) # Добавить организаторов события - карточки пользователей из контактов.
    participants = models.ManyToManyField(User, related_name='event_participants', blank=True) # Добавить участников событий - карточки исполнителей.


class Project(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200) # название
    link = models.URLField(max_length=500, blank=True, null=True) #Ссылка
    access = models.CharField(max_length=20, choices=[ # Доступ. Единичный выбор: - для всех;- только я.
        ('all', 'For all'),
        ('me', 'Only me')
    ], default='all')
    reminder_events = models.BooleanField(default=False) #  Напоминание о событиях - чекбокс
    comment = models.TextField(blank=True) # Комментарий
    personal_note = models.TextField(blank=True) # Личная заметка
    organizers = models.ManyToManyField(User, related_name='project_organizers',blank=True) # Добавить организаторов события - карточки пользователей из контактов.
    participants = models.ManyToManyField(User, related_name='project_participants', blank=True) # Добавить участников событий - карточки исполнителей.




