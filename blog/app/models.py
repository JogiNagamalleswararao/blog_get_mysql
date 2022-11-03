from django.db import models
from datetime import datetime
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/")
    describe=models.CharField(max_length=100)
    create_at=models.DateTimeField(default=datetime.now)
    def __str__(self) -> str:
        return self.title

