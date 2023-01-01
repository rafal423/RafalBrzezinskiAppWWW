from rest_framework import serializers
from .models import Osoba, Druzyna

class DruzynaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(max_length=64, allow_blank=False)
    kraj = serializers.CharField(max_length=2, allow_blank=False)

    def create(self, validated_data):
        return Druzyna.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.kraj = validated_data.get('kraj', instance.kraj)
        instance.save()
        return instance

class OsobaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(max_length=50, allow_blank=False)
    nazwisko = serializers.CharField(max_length=100, allow_blank=False)
    miesiac_urodzenia = serializers.ChoiceField(choices=Osoba.Miesiace.choices, default=Osoba.Miesiace.STYCZEN)
    druzyna = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all(),allow_null=True)

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.miesiac_urodzenia = validated_data.get('miesiac_urodzenia', instance.miesiac_urodzenia)
        instance.druzyna = validated_data.get('druzyna', instance.druzyna)
        instance.save()
        return instance