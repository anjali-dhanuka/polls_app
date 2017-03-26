from django.db import models

# Create your models here.

class Question(models.Model):
    question_text=models.TextField(max_length=300)
    pub_date=models.DateTimeField('date published')

    def __unicode__(self):
        return str(self.question_text)


class Choice(models.Model):
    question=models.ForeignKey(Question)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.choice_text)

#def __str__(self):
 #  return self.question_text
#def__str__(self):

