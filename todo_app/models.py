from django.db import models

# Create your models here.


class TodoModel(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(null=True,blank=True)
    status=models.BooleanField(default=True)
    create_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title}"