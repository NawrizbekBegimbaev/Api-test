from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField('Имя',max_length=45)
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Пользователь'

class Calendar(models.Model):
    userId = models.ForeignKey('User',on_delete=models.CASCADE,)
    name = models.CharField('Название',max_length=45)
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name_plural = 'Календарь'

class Event(models.Model):
    userId = models.ForeignKey('User',on_delete=models.CASCADE,)
    calendarId = models.ForeignKey('Calendar',on_delete=models.CASCADE,)
    name = models.CharField('Название',max_length=200)
    location = models.CharField('Локация',max_length=200)
    start = models.DateTimeField('Начало')
    end = models.DateTimeField('Конец')
    
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Заметка'

class Invites(models.Model):
    userId = models.ForeignKey('User',on_delete=models.CASCADE,)
    eventId = models.ForeignKey('Event',on_delete=models.CASCADE,)

    class Meta:
        verbose_name_plural = 'Приглашение'