from django.db import models
from django.contrib.auth.models import User


class students(models.Model):
    all_branches = (
        ('1', 'IT'),
        ('2', 'Comp'),
        ('3', 'Chemical'),
        ('4', 'Mechanical'),
        ('5', 'Civil'),
        ('6', 'EnTc'),
        ('7', 'ETX')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year = models.IntegerField(blank=False, default=2016)
    branch = models.CharField(max_length=20, choices=all_branches, blank= False)
    prn = models.CharField(blank=False, max_length=10)

    def __str__(self):
        return self.user.username


class books(models.Model):
    isbn = models.CharField(blank=False, max_length=50)
    title = models.CharField(blank=False, max_length=50)
    author = models.CharField(blank=False, max_length=50)
    published = models.CharField(blank=False, max_length=4)
    price = models.FloatField(blank=False)
    quantity = models.IntegerField(blank=False, default=1)

    def __str__(self):
        return self.title


class borrowed(models.Model):
    issedby = models.ForeignKey(students, on_delete=models.CASCADE)
    issuedate = models.DateField(auto_now_add=True)
    book = models.ForeignKey(books, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title
