from rest_framework import serializers
from publishers.serializers import PublisherSerializer
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = '__all__'

        def create(self, validated_data):
            book = Book(**validated_data)
            book.save()
            return book

        def update(self, instance, validated_data):
            instance.name = validated_data.get(
                'name', instance.name
            )
            instance.username = validated_data.get(
                'username', instance.username
            )
            instance.publication_date = validated_data.get(
                'publication_date', instance.publication_date
            )
            instance.publisher = validated_data.get(
                'publisher', instance.publisher
            )
            instance.description = validated_data.get(
                'description', instance.description
            )

            instance.save()
            return instance
