from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 225)

    def __str__(self):
        return self.name


class Quizes(models.Model):
    category = models.ForeignKey(Category, default = 1, on_delete = models.SET_NULL, null = True)
    class Meta:
        verbose_name = ('Quiz')
        verbose_name_plural = ('Quizzes')
        ordering = ['id']


class UpdatedQuestions(models.Model):
    updated_date = models.DateTimeField(auto_now = True)
    class Meta:
       abstract = True

class Questions(UpdatedQuestions):
    quiz = models.ForeignKey(Quizes, on_delete = models.CASCADE)
    class Meta:
        verbose_name = ('Question')
        verbose_name_plural = ('Questions')
        ordering = ['id']


class Answers(UpdatedQuestions):
    question = models.ForeignKey(Questions, on_delete = models.CASCADE)
