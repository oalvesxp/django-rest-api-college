from django.db import models

class Student(models.Model):
    name = models.CharField(max_lenght=30)
    rg = models.CharField(max_lenght=9)
    cpf = models.CharField(max_lenght=11)
    birth = models.DateField()

    def __str__(self):
        return self.name