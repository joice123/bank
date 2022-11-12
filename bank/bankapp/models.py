from django.db import models




# Create your models here.
class Programming(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    programming = models.ForeignKey(Programming,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

ACCOUNT_CHOICES=(
    ('C','Cheque'),
    ('D','Debit Card'),
    ('C','Credit Card'),
)

class Bank(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField()
    number=models.IntegerField()
    dob=models.DateField()
    add=models.CharField(max_length=300)
    account=models.CharField(choices=ACCOUNT_CHOICES,max_length=255)


    def __str__(self):
        return self.name


