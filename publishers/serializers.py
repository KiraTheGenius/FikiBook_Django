from rest_framework import serializers
from .models import Publisher


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

    def create(self, validated_data):
        publisher = Publisher(**validated_data)
        publisher.save()
        return publisher

    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name', instance.name
        )
        instance.description = validated_data.get(
            'description', instance.description
        )

        instance.save()
        return instance
