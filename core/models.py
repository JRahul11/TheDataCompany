from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Technology(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = 'Technologies'
    
    def __str__(self):
        return self.name


class ExpertiseLevel(models.Model):
    level = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = 'Expertise Level'
    
    def __str__(self):
        return self.level
    

class UserTechStack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    technology = models.ForeignKey(Technology, on_delete=models.SET_NULL, null=True)
    expertise_level = models.ForeignKey(ExpertiseLevel, on_delete=models.SET_NULL, null=True)
    learning_resource = models.CharField(max_length=50, null=True)
    
    class Meta:
        verbose_name_plural = 'Users Tech Stack'

    def __str__(self):
        return self.user.username + ' ' + self.category.name + ' ' + self.technology.name
