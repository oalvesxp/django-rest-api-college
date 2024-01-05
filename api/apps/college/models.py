from django.db import models

class Student(models.Model):
    name = models.CharField(max_lenght=30)
    rg = models.CharField(max_lenght=9)
    cpf = models.CharField(max_lenght=11)
    birth = models.DateField()

    def __str__(self):
        return self.name

class Course(models.Model):
    LEVEL = {
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    }

    code_course = models.CharField(max_lenght=10)
    description = models.CharField(max_lenght=100)
    level = models.CharField(
        max_lenght=1, 
        choices=LEVEL, 
        blank=False, 
        null=False, 
        default='B'
    )

    def __str__(self):
        return self.description