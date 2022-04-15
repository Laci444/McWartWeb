from tabnanny import verbose
from django.db import models

# Create your models here.
class newModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news/%Y/%m/%d/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
     
    class Meta:
        verbose_name_plural = 'Hírek'
        verbose_name = 'Hír'
