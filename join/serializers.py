from rest_framework import serializers
from .models import Contact, SubTaskItem, TaskItem, Category
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTaskItem
        fields = ['title', 'completed']

class TaskItemSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all(), many=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    subtasks = SubtaskSerializer(many=True, required=False)

    class Meta:
        model = TaskItem
        fields = '__all__'
    
    def create(self, validated_data):
        assigned_to_data = validated_data.pop('assigned_to', [])
        subtasks_data = validated_data.pop('subtasks', [])
        task = TaskItem.objects.create(**validated_data)
        task.assigned_to.set(assigned_to_data)
        for subtask_data in subtasks_data:
            SubTaskItem.objects.create(parent_task=task, **subtask_data)
        return task
    
    def update(self, instance, validated_data):
        # Update the non-nested fields
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.category = validated_data.get('category', instance.category)
        instance.save()

        # Update the assigned_to field
        if 'assigned_to' in validated_data:
            assigned_to_data = validated_data.pop('assigned_to')
            instance.assigned_to.set(assigned_to_data)

        # Update the subtasks field
        if 'subtasks' in validated_data:
            subtasks_data = validated_data.pop('subtasks')
            # Clear existing subtasks
            instance.subtasks.all().delete()
            # Create new subtasks
            for subtask_data in subtasks_data:
                SubTaskItem.objects.create(parent_task=instance, **subtask_data)

        return instance

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def create(self, validated_data):
        contact = Contact.objects.create(**validated_data)
        return contact
