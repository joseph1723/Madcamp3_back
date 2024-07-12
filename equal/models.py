from django.db import models

class Player(models.Model):
    user_id = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    highscore = models.IntegerField()
    item = models.JSONField(default = list)
    gold = models.IntegerField()
    email = models.EmailField(null=True, blank=True) 

    def __str__(self):
        return f"{self.user_id} {self.gold}"
class Problem(models.Model):
    num = models.CharField(max_length = 4)
    difficulty = models.IntegerField()

    def __str__(self):
        return f"{self.num} {self.difficulty}"

# Create your models here.
