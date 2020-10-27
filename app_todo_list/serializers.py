import json
from rest_framework.serializers import ModelSerializer
from app_todo_list.models import Tasks


class CustomSerializer(ModelSerializer):
    """
    Custom Serializer
    """
    def create(self, validated_data):
        """
        Create and return a new `Clients` instance, given the validated data
        """
        # Create main Object
        main_object = self.__class__.Meta.model.objects.create(**validated_data)
        # Return object created
        return main_object


class TasksSerializer(CustomSerializer):
    """
    Clients serializer
    """
    class Meta:
        model = Tasks
        fields = '__all__'
