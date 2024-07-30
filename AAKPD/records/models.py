from django.db import models


class violations(models.Model):

    date = models.DateTimeField('Дата и время')
    fio = models.CharField('ФИО', max_length=250)
    description = models.TextField('Суть')
    photo = models.BinaryField('Фото')

    #def __str__(self):
     #   return self.fio
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
