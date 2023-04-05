from django.db import models

# Create your models here.


class Departament(models.Model):
    name = models.CharField(max_length=50)

    created_on = models.DateTimeField('Created on', auto_now_add= True, null= True)
    updated_on = models.DateTimeField('Updated on', auto_now= True, null= True)

    def __str__(self):
        return f'{self.name}'
    

class Collaborator(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE, related_name='collaborators')

    created_on = models.DateTimeField('Created on', auto_now_add= True, null= True)
    updated_on = models.DateTimeField('Updated on', auto_now= True, null= True)

    def __str__(self):
        return f'{self.name}'
    