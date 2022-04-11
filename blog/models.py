
from django.db import models
from django.utils import timezone
from django.urls import  reverse
from django.contrib.auth import get_user_model

User=get_user_model()


# Create your models here.
class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text = models.TextField()
    created_date=models.DateTimeField(default=timezone.now())
    published_date=models.DateTimeField(blank=True,null=True)
    likes=models.ManyToManyField(User,related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()
        

    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey('blog.Post',on_delete=models.CASCADE,related_name='comments')
    author=models.CharField(max_length=100)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    approved_comment=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()
    def get_absolute_url(self):
        return reverse('post_list')
    def __str__(self):
        return self.text
