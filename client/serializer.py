from client.models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
class institutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = institution
        fields = "__all__"

class degreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = degree
        fields = "__all__"

class field_of_studySerializer(serializers.ModelSerializer):
    class Meta:
        model = field_of_study
        fields = "__all__"

class educationSerializer(serializers.ModelSerializer):
    class Meta:
        model = education
        fields = "__all__"

class feedSerializer(serializers.ModelSerializer):
    class Meta:
        model = feed
        fields = "__all__"

class imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = image
        fields = "__all__"

class interactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = interaction
        fields = "__all__"

class groupSerializer(serializers.ModelSerializer):
    class Meta:
        model = group
        fields = "__all__"

class group_membershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = group_membership
        fields = "__all__"

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = "__all__"

class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = "__all__"