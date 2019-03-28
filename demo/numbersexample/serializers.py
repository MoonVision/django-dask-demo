from rest_framework import serializers

from numbersexample.models import Number


class NumberSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Number
        fields = ('url', 'value')
