from rest_framework import serializers
from .models import *


# create you serializer
class InlineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InlineItem
        fields = '__all__'


class MasterItemBatchSerializer(serializers.ModelSerializer):
    inline_items = InlineItemSerializer(many=True, read_only=True)

    class Meta:
        model = MasterItem
        fields = '__all__'
        read_only_fields = ['id']

