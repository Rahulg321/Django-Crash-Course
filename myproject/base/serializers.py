from rest_framework import serializers
from .models import Task


# converting an object into a byte form and rendering it out in json format
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        """
            Model Meta is basically used to change the behavior of your model fields like changing order options,verbose_name, and a lot of other options. It’s completely optional to add a Meta class to your model
        """
        model = Task
        fields = '__all__'
