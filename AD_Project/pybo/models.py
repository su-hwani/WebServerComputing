from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')
    # <<< AD project first
    modify_count = models.IntegerField(null=True, blank=True, default=0)
    # >>>

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')
    # <<< AD project 1
    modify_count = models.IntegerField(null=True, blank=True, default=0)
    # >>>


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(
        Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(
        Answer, null=True, blank=True, on_delete=models.CASCADE)
    # <<< AD project 3
    voter = models.ManyToManyField(User, related_name='voter_comment')
    # >>>
    # <<< AD project 4
    modify_count = models.IntegerField(null=True, blank=True, default=0)
    # >>>
