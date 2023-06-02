from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import  reverse

class Category(models.Model):
    name=models.CharField(max_length=150,db_index=True)
    slug=models.SlugField(unique=True,blank=True)
    class Meta:
        ordering=('-name',)
    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug  = slugify(self.name)
        super(Category,self).save(*args,**kwargs) 

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])
    




class Post(models.Model):
    category = models.ForeignKey(Category , related_name='post' , on_delete=models.CASCADE)
    user = models.ForeignKey(User , related_name='user',  on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/') 
    

    def __str__(self):
        return self.title
