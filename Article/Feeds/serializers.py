

from rest_framework import serializers

from Article.settings import LOGIN_URL
from .models import *
from .models import *
    
        
class Articleserializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source = 'article_user.username')
    class Meta:
        model = Article
        fields = ['user','title','feature_image','description','like','name']
        
        
        def create(self,validated_data):
            
            post = Article.objects.create(**validated_data)
            return post
        
class Followersserializer(serializers.ModelSerializer):
#    name = serializers.ReadOnlyField(source = 'follower.username')
    class Meta:
        model = Followers
        fields = ['name','follower']
        
    def create(self,validated_data):
        
        followers = Followers.objects.create(**validated_data)
        return followers
        
        
class Draftserializer(serializers.ModelSerializer):
   # name = serializers.ReadOnlyField(source = 'save_name.username')
    class Meta:
        model = Draft
        fields = ['name','post']
        
    def create(self,validated_data):
        save = Draft.objects.create(**validated_data)
        return save


class commentserializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source = 'name.username')
   
    class Meta:
        model = Comment
        fields = ['comment','name','artticle']
        
    
    def create(self,validated_data):
        
        save = Comment.objects.create(**validated_data)
        return save
