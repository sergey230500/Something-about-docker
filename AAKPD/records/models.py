from django.db import models
import base64

class violations(models.Model):

    date = models.DateTimeField('Дата и время')
    fio = models.CharField('ФИО', max_length=250)
    description = models.TextField('Суть')
    photo = models.BinaryField('Фото')

    def __str__(self):
        return self.fio
    
    def get_image_as_base64(self):
        return 'data:image/jpeg;base64,' + base64.b64encode(self.photo).decode('utf-8')
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
