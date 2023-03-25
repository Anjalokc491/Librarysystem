from rest_framework import serializers
from .models import BookList,community

class sampleform(serializers.ModelSerializer):
    class Meta:
        model = community,BookList
        fields = '__all__'
