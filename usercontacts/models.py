from django.db import models

# Create your models here.
class Contact(models.Model):
    owner = models.ForeignKey("auth.User")
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=50, blank=True)
    
    def __str__(self):
        return self.last_name + "," + self.first_name