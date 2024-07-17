# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
# from django.utils import timezone

# class CustomUserManager(BaseUserManager):
#     def create_user(self, user_id, password=None, **extra_fields):
#         if not user_id:
#             raise ValueError('The User ID must be set')
#         user = self.model(user_id=user_id, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, user_id, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(user_id, password, **extra_fields)

# class Player(AbstractBaseUser, PermissionsMixin):
class Player(models.Model):
    user_id = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=30)
    highscore = models.IntegerField(default = 0)
    item = models.JSONField(default=list)
    gold = models.IntegerField(default = 0)
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user_id} {self.nickname} {self.email}"
    
    def update_score_if_higher(self, new_score):
        if new_score > self.highscore:
            self.highscore = new_score
            self.save()

class Problem(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.CharField(max_length = 4)
    difficulty = models.IntegerField()
    

    def __str__(self):
        return f"{self.id} {self.num} {self.difficulty}"

class Rank(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user_id} - {self.score}"

    def update_score_if_higher(self, new_score):
        if new_score > self.score:
            self.score = new_score
            self.save()
# Create your models here.
