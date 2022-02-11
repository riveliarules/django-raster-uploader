from django.db import models

class Rasterfile(models.Model):
    file_name = models.CharField(max_length=100)
    file_workspace = models.CharField(max_length=100)
    file_archive = models.FileField(upload_to='')

    def __str__(self):
        return self.file_name

