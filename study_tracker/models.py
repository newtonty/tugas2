from django.db import models

# Create your models here.
class Assignment (models.Model):
    name = models.CharField(max_length=(50))
    subject = models.CharField(max_length=(50))
    date = models.DateTimeField()
    progress = models.IntegerField()
    description = models.TextField()

    #mengubah nama Assignment object menjadi name pada admin
    def __str__(self):
        return "{}".format(self.name)
