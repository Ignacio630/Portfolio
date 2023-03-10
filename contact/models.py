from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ['-created']

    def __str__(self):
        return self.name