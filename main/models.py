import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Bar_code(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    charge = models.IntegerField()

    def __str__(self):
        return self.name

class Review(models.Model):
    code_name = models.ForeignKey(Bar_code, on_delete=models.CASCADE) # 외래키이므로 위에 question을 참조하고 삭제되면 같이 삭제
    review_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.review_text

class Img(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/%Y/%M/%D')

    def __str__(self):
        return self.title

class Imgadd(models.Model):
    code_img = models.ImageField(upload_to='images/%Y/%M/%D')
    name = models.CharField(max_length=30)
    charge = models.IntegerField()

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 외래키이므로 위에 question을 참조하고 삭제되면 같이 삭제
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text