from rest_framework import serializers
from singerapp.models import *

class LabelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labels
        fields = ('name', 'date', 'people')

class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ('name', 'date', 'people', 'labels')

class FeedbackSerializer(serializers.ModelSerializer):
    ch = (
        (0, 'like'),
        (1, 'dislike'),
    )
    like_dislike = serializers.ChoiceField(choices=ch)
    class Meta:
        model = Feedback
        fields = ('like_dislike', 'comments',)

class SingersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singers
        fields = ('name', 'age', 'nationality', 'groups', 'rate',)

class Solo_singerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solo_singer
        fields = ('name', 'date', 'people', 'labels')


