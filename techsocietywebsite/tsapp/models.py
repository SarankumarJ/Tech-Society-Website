from django.db import models

# Create your models here.

class Community(models.Model):
    name = models.CharField(max_length=100,)
    discription = models.TextField(default='')

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Year(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class PRTeam(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    prteam = models.ForeignKey(PRTeam, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
