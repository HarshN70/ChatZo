from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self) -> str:
        return self.content[:50]

class friends(models.ForeignKey):
    person1 = models.ForeignKey(User, on_delete=models.CASCADE)
    person2 = models.ForeignKey(User, on_delete=models.CASCADE)