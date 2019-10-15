from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    technology = models.CharField(max_length=255) # comma separated tags, best practice is using a different table.
    url = models.URLField()
    #image = models.FilePathField(path="static/portfolio/img", blank=True, null=True)
    image = models.ImageField(upload_to='portfolio/img', blank=True, null=True)
    demo = models.URLField(blank=True, null=True)
    date = models.DateField(u"Project Finish Date", blank=True, null=True)