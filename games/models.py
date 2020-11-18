from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
def image_upload(instance,filename):
    imagename,extension = filename.split('.')
    return "games/%s.%s"%(instance.title,extension)

class Game(models.Model):
    title = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload,default='')
    content = models.TextField()
    description = models.TextField()
    keywords = models.TextField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.email
    

