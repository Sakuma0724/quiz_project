from django.db import models
 
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_image = models.ImageField(upload_to='question_images/', blank=True, null=True)
    correct_choices = models.ManyToManyField('Choice', related_name='correct_for')
    explanation = models.CharField(max_length=200)
    correct_number = models.CharField(max_length=200)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
