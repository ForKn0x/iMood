from rest_framework import generics
from mood.models import Mood, FeelingsTag, ReasonsTag
from .serializers import moodSerializer, reasonsTagsSerializer, feelingsTagsSerializer
from rest_framework.permissions import IsAuthenticated


#######################--------------------- Mood Model ---------------------#######################

class MoodView(generics.ListCreateAPIView):
        queryset = Mood.objects.all()
        serializer_class = moodSerializer
        permission_classes = [IsAuthenticated]
        
        def get_queryset(self):
                user = self.request.user
                userFilter = Mood.objects.filter(created_by=user)
                return userFilter

class MoodDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Mood.objects.all()
        serializer_class = moodSerializer
        lookup_field = 'id'
        permission_classes = [IsAuthenticated]
        

#######################--------------------- Reason Tag Model ---------------------#######################
class reasonsTagsView(generics.ListCreateAPIView):
        queryset = ReasonsTag.objects.all()
        serializer_class = reasonsTagsSerializer
        permission_classes = [IsAuthenticated]
        
        def get_queryset(self):
                user = self.request.user
                userFilter = ReasonsTag.objects.filter(created_by=user)
                adminFilter = ReasonsTag.objects.filter(created_by=1)
                finalFilter = userFilter | adminFilter
                return finalFilter
        
class reasonsTagsDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = ReasonsTag.objects.all()
        serializer_class = reasonsTagsSerializer
        lookup_field = 'id'
        permission_classes = [IsAuthenticated]
        
#######################--------------------- Feelings Tag Model ---------------------#######################
        
class feelingsTagsView(generics.ListCreateAPIView):
        queryset = FeelingsTag.objects.all()
        serializer_class = feelingsTagsSerializer
        permission_classes = [IsAuthenticated]
        
        def get_queryset(self):
                user = self.request.user
                userFilter = FeelingsTag.objects.filter(created_by=user)
                adminFilter = FeelingsTag.objects.filter(created_by=1)
                finalFilter = userFilter | adminFilter
                return finalFilter
        
class feelingsTagsDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = FeelingsTag.objects.all()
        serializer_class = feelingsTagsSerializer
        lookup_field = 'id'
        permission_classes = [IsAuthenticated]
        