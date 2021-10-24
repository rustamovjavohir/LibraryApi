from django.core import serializers
from books.models import Reader, Kartoteka


def Reader_obj(pk):
    obj_json = serializers.serialize('json', Reader.objects.filter(id=pk), fields=('first_name', 'last_name'))
    return obj_json


def Kartoteka_obj(reader_id: int = None, reader_name: str = None):
    if reader_id:
        obj_json = serializers.serialize('json', Kartoteka.objects.filter(reader_id=reader_id).distinct('book__title',
                                                                                                        'book__author'),
                                         fields=('book',))

    return obj_json
