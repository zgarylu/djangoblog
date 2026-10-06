from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Language(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Programmer(models.Model):
    name = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='programmers')
    languages = models.ManyToManyField(Language, related_name='programmers')
    def __str__(self):
        return self.name
class Todo(models.Model):
    title = models.CharField(max_length=40)
    detail = models.TextField()
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        status = "Completed" if self.complete else "Pending"
        return f"{self.title} | {status} | {self.created_date:%Y-%m-%d %H:%M}"