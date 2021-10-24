from rest_framework import serializers
from rest_framework.utils.field_mapping import get_nested_relation_kwargs
from books.models import Book, Reader, Kartoteka


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'page_count', 'year', 'category']


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ['first_name', 'last_name', 'profession']


class KartotekaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kartoteka
        fields = ['book', 'reader']
        depth = 1

    def build_nested_field(self, field_name, relation_info, nested_depth):
        if field_name == 'book':
            field_class = BookSerializer
            field_kwargs = get_nested_relation_kwargs(relation_info)
            return field_class, field_kwargs
        if field_name == 'reader':
            field_class = ReaderSerializer
            field_kwargs = get_nested_relation_kwargs(relation_info)
            return field_class, field_kwargs
        return super().build_nested_field(field_name, relation_info, nested_depth)
