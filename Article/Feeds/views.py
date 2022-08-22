from rest_framework import generics
from django.shortcuts import render
from .models import *
from .serializers import  *
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from dj_rest_auth.views import LoginView,LogoutView
from dj_rest_auth.serializers import LoginSerializer

# I didnt Implemented full frontend only some stuff 
#which might know about my knowledge


class Login(LoginView):
    serializer_class = LoginSerializer
    renderer_classes = [TemplateHTMLRenderer,JSONRenderer]
    template_name  = "n/login.html"      
    
    def get(self,request):
        
        return render(request,self.template_name)
 
class post(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = Articleserializer
        


class postList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = Articleserializer(many=True)
    renderer_classes = [TemplateHTMLRenderer,JSONRenderer]
    template_name  = "Feeds/feed.html"
    
    def get(self,request):
        queryset = Article.objects.all()
        return Response({'data': queryset})
            
        
       
 
class Followers(generics.ListCreateAPIView):
    queryset = Followers.objects.all()
    serializer_class = Followersserializer   
    
     
    
class comment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = commentserializer
    


class Draft(generics.ListCreateAPIView):
    queryset = Draft.objects.all()
    serializer_class = Draftserializer
    

class Edit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = Articleserializer
   
   
    
    
    
    