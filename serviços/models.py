from django.db import models

class serviço(models.Model):
        Nome = models.CharField(max_length=500, null=True)

        def __str__(self):
                return self.Nome