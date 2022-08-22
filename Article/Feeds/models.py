from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# I didndt used string because it ias just a demo purpose

class Article(models.Model):
    title = models.CharField(max_length=10000)
    feature_image = models.ImageField(upload_to='post')
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='article_user')
    like = models.ForeignKey(User,on_delete=models.CASCADE,related_name='nap_like')
    
    def total_like(self):
        return self.total_like.count()
    
    
    
class Followers(models.Model):
    follower =  models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    name =  models.ForeignKey(User,on_delete=models.CASCADE)
    
    
class Draft(models.Model):
    post = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='save_name')
    

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    artticle = models.ForeignKey(Article,on_delete=models.CASCADE)
    
    
        
