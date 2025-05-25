from rest_framework import serializers
from .models import Hit

class HitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hit
        fields = ['id', 'title', 'artist', 'title_url', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'title_url']  # Te pola generujemy automatycznie

    def create(self, validated_data):
        # Tworzymy obiekt i automatycznie generujemy title_url (czyli wersję tytułu bez spacji i małymi literami)
        instance = super().create(validated_data)
        instance.title_url = instance.title.lower().replace(" ", "-")
        instance.save()
        return instance

    def update(self, instance, validated_data):
        # Przy aktualizacji — jeśli zmieniono tytuł, to zmieniamy też title_url
        if 'title' in validated_data:
            instance.title_url = validated_data['title'].lower().replace(" ", "-")
        return super().update(instance, validated_data)