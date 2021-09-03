from rest_framework import serializers
from collections import OrderedDict 
from django.contrib.auth.models import update_last_login
from .models import (
    RetrivedData,
    ProcessData
)




class RetrivedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetrivedData
        fields = [field.name for field in RetrivedData._meta.local_fields if field.name != 'id']