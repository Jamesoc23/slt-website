from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings


image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}'.format(settings.MEDIA_URL),
)

def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/my_sell/picture/<filename>
    return u'picture/{0}'.format(filename)

class Service(models.Model):
    title = models.CharField(max_length=100, default='')
    body = models.TextField()
    image = models.ImageField(upload_to=image_directory_path, storage=image_storage, blank=True, null=True)

    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    social = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class About(models.Model):
    about = models.TextField()

    def __str__(self):
        return self.about