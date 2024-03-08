from rest_framework import viewsets
from client import models
from client import serializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserSerializer

class institutionViewSet(viewsets.ModelViewSet):
    queryset = models.institution.objects.all()
    serializer_class = serializer.institutionSerializer

class degreeViewSet(viewsets.ModelViewSet):
    queryset = models.degree.objects.all()
    serializer_class = serializer.degreeSerializer

class field_of_studyViewSet(viewsets.ModelViewSet):
    queryset = models.field_of_study.objects.all()
    serializer_class = serializer.field_of_studySerializer

class educationViewSet(viewsets.ModelViewSet):
    queryset = models.education.objects.all()
    serializer_class = serializer.educationSerializer

class feedViewSet(viewsets.ModelViewSet):
    queryset = models.feed.objects.all()
    serializer_class = serializer.feedSerializer

class imageViewSet(viewsets.ModelViewSet):
    queryset = models.image.objects.all()
    serializer_class = serializer.imageSerializer

class interactionViewSet(viewsets.ModelViewSet):
    queryset = models.interaction.objects.all()
    serializer_class = serializer.interactionSerializer

class groupViewSet(viewsets.ModelViewSet):
    queryset = models.group.objects.all()
    serializer_class = serializer.groupSerializer

class group_membershipViewSet(viewsets.ModelViewSet):
    queryset = models.group_membership.objects.all()
    serializer_class = serializer.group_membershipSerializer

class postViewSet(viewsets.ModelViewSet):
    queryset = models.post.objects.all()
    serializer_class = serializer.postSerializer

class eventViewSet(viewsets.ModelViewSet):
    queryset = models.event.objects.all()
    serializer_class = serializer.eventSerializer