from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 225, verbose_name = "Name")
    class Meta:
        verbose_name = ('category')
        verbose_name_plural = ('Categorys')
        ordering = ['id']
    
    def __str__(self):
        return self.name


class Quiz(models.Model):
    category = models.ForeignKey(Category, default = 1, on_delete = models.SET_NULL, null = True)
    title = models.CharField(max_length = 225, default = "New Quiz", verbose_name = "Quiz Title")
    data_created = models.DateTimeField(auto_now_add = True, null=True , verbose_name = 'Date Created')
    class Meta:
        verbose_name = ('Quiz')
        verbose_name_plural = ('Quizzes')
        ordering = ['id']
    
    def __str__(self):
        return self.title


class Updated(models.Model):
    updated_date = models.DateTimeField(auto_now = True, verbose_name = "last updated")
    class Meta:
       abstract = True

class Question(Updated):

    scale = (
        (0,'Fundamental'),
        (1,'Beginner'),
        (2,'Intermediate'),
        (3,'Advanced'),
        (4,'Expert')  
    )

    type = (
        (0, 'Multiple Choice'),
    )

    title = models.CharField(max_length = 255, verbose_name = 'Title', null = True)
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    level = models.IntegerField(default = 0, choices = scale, verbose_name = 'Level' )
    technique = models.IntegerField(default = 0 , choices = type, verbose_name = "Question Type" )
    data_created = models.DateTimeField(auto_now_add = True,  null=True, verbose_name = 'Date_created')
    is_active = models.BooleanField (default = True, verbose_name = 'Active Status')

    class Meta:
        verbose_name = ('Question')
        verbose_name_plural = ('Questions')
        ordering = ['id']


class Answer(Updated):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    answer_text = models.CharField (max_length = 255, verbose_name= 'Answer Text' , null = True)
    is_right = models.BooleanField(default = False)

    class Meta:
        verbose_name = ('Answer')
        verbose_name_plural = ('Answers')
        ordering = ['id']

    def __str__(self):
        return self.answer_text

