from rest_framework import serializers
from .models import coders

class CodersSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    student_ID = serializers.CharField(max_length=200)
    date_created = serializers.ReadOnlyField()
    image = serializers.URLField()   
    current_role = serializers.CharField(max_length=200)
    tech_industry = serializers.BooleanField() 
    programs_complete = serializers.CharField(max_length=200)
    programs_interested = serializers.CharField(max_length=200)
    location = serializers.CharField(max_length=200)
    mentoring = serializers.CharField(max_length=200)
    partner_hire = serializers.CharField(max_length=200)
    post_study = serializers.BooleanField()
      
    #this will be called for POST /projects to create a new projects
    def create(self, validated_data):
        return coders.objects.create(**validated_data)

class CodersDetailSerialiser(CodersSerializer):
    def update(self, instance, validated_data):
        instance.student_ID = validated_data.get('student_ID', instance.student_ID)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.image = validated_data.get('image', instance.image)
        instance.current_role = validated_data.get('current_role', instance.current_role)
        instance.tech_industry = validated_data.get('tech_industry', instance.tech_industry)
        instance.programs_complete = validated_data.get('programs_complete', instance.programs_complete)
        instance.programs_interested = validated_data.get('programs_interested', instance.programs_interested)
        instance.location = validated_data.get('location', instance.location)
        instance.mentoring = validated_data.get('mentoring', instance.mentoring)
        instance.partner_hire = validated_data.get('partner_hire', instance.partner_hire)
        instance.post_study = validated_data.get('post_study', instance.post_study)
        instance.save()
        return instance