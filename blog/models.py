
from django.db import models
from django.utils import timezone
from django.urls import  reverse
from django.contrib.auth import get_user_model
from sqlalchemy import null, true
from PIL import Image
from tinymce.models import HTMLField
User=get_user_model()


# Create your models here.
class Post(models.Model):
    # author=models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    title=models.CharField(max_length=200)
    short_desc=models.TextField(default=True)
    text = HTMLField()
    image=models.ImageField(upload_to='profile_pics',null=True)
    created_date=models.DateTimeField(default=timezone.now())
    published_date=models.DateTimeField(blank=True,null=True)
    likes=models.ManyToManyField(User,related_name='blog_posts')
    home=models.BooleanField(help_text="select this blog for home page",default=False)
    def total_likes(self):
        return self.likes.count()
        
    def home1(self):
        self.home=True
        self.save()
    def owner1(self):
        self.owner=True
        self.save()
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        # run the parent class' save() function:
        super().save(*args, **kwargs)

        # open the image of the current instance:
        image = Image.open(self.image.path)

        if image.height > 425 or image.width > 425:
            output_size = (425, 425)
            image.thumbnail(output_size)
        image.save(self.image.path)

class Comment(models.Model):
    post=models.ForeignKey('blog.Post',on_delete=models.CASCADE,related_name='comments')
    # author=models.ForeignKey(UserWarning,on_delete=models.CASCADE,default=True)
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

