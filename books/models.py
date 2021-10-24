from django.db import models
from datetime import datetime, timedelta


# Create your models here.


class AbstractClass(models.Model):
    created_at = models.DateTimeField(default=datetime.now())
    created_by = models.IntegerField(default=-1)
    is_deleted = models.IntegerField(default=0)
    deleted_by = models.IntegerField(default=-1)

    class Meta:
        abstract = True


class Book(AbstractClass):
    title = models.CharField(max_length=200, null=False, blank=False)
    author = models.CharField(max_length=200, null=False, blank=False)
    page_count = models.IntegerField()
    year = models.DateTimeField(default=datetime.now())
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Reader(AbstractClass):
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    is_active = models.IntegerField(default=1)

    def __str__(self):
        return self.first_name


class Employee(AbstractClass):
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    Role = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.last_name[0].upper()}.{self.first_name.capitalize()}'


class Kartoteka(AbstractClass):
    book = models.ForeignKey(Book, related_name='book_id', on_delete=models.DO_NOTHING)
    reader = models.ForeignKey(Reader, on_delete=models.DO_NOTHING)
    employee_id = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    get_time = models.DateTimeField(default=datetime.now())
    return_time = models.DateTimeField(default=datetime.now() + timedelta(days=15))

    def __str__(self):
        return f'{self.book.title}: {self.return_time}'
