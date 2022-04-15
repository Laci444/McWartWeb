from django.db import models

# Create your models here.
class pageModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='pages/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Oldalak'
        verbose_name = 'Oldal'