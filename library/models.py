from django.db import models

# Create your models here.

class login(models.Model):

    username=models.CharField(max_length=25)
    password=models.IntegerField()

    def __str__(self):
        return self.username

class register(models.Model):

    Email=models.CharField(max_length=25)
    Age=models.IntegerField()
    Adress=models.CharField(max_length=25)
    def __str__(self):
        return self.Email

class BookList(models.Model):

    BookName=models.CharField(max_length=25)
    BookNumber=models.IntegerField()

    def __str__(self):
        return self.BookName


class UsedBookList(models.Model):
    BookName = models.CharField(max_length=25)
    BookNumber = models.IntegerField()

    def __str__(self):
        return self.UsedBookName

class community(models.Model):
    Name = models.CharField(max_length=25)
    PhoneNumber = models.IntegerField()
    def __str__(self):
        return self.Name

