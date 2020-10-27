from django.db import models


class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    category = models.IntegerField()
    blog_slug = models.CharField(max_length=50)
    blog_content = models.TextField()
    created_date = models.DateTimeField()
    author_uid = models.IntegerField()

    class Meta:
        ordering = ['-created_date']
        db_table = 'blog_post'

    def __str__(self):
        return self.title
