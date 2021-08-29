from django.db import models
from django.contrib.auth import get_user_model

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE #deletes stories if an author is deleted
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    img_upload = models.ImageField(upload_to='images')
    
    # class Meta:
    #     ordering = ['-pub_date']
    # ordered through views instead
