from django.db import models


class Test(models.Model):
    PSYCHOLOGICAL = 'PS'
    ENTERTAINING = 'EN'
    EDUCATIONAL = 'ED'
    TEST_TYPE_CHOICES = [
        (PSYCHOLOGICAL, 'Психологический'),
        (ENTERTAINING, 'Развлекательный'),
        (EDUCATIONAL, 'Образовательный'),
    ]
    name = models.CharField(max_length=200)
    is_private = models.BooleanField(default=False)
    category = models.CharField(
        max_length=2,
        choices=TEST_TYPE_CHOICES,
    )
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

    def save_changes(self):
        self.save()

    def __str__(self):
        return self.name


class Question(models.Model):
    MULTIPLE = 'M'
    SINGLE = 'S'
    QUESTION_TYPE_CHOICES = [
        (MULTIPLE, 'Множественный'),
        (SINGLE, 'Одиночный'),
    ]
    test = models.ForeignKey('tests.Test', on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    type = models.CharField(
        max_length=1,
        choices=QUESTION_TYPE_CHOICES,
        default=SINGLE,
    )

    def save_question(self):
        self.save()

    def __str__(self):
        return self.text

    def create_label(self):
        return f'q{self.pk}'


class Answer(models.Model):
    question = models.ForeignKey('tests.Question', on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    value = models.IntegerField()
    image = models.ImageField(upload_to='images/answers/', blank=True)

    def save_answer(self):
        self.save()

    def __str__(self):
        return self.text

    def create_label(self):
        return f'a{self.pk}'


class Result(models.Model):
    test = models.ForeignKey('tests.Test', on_delete=models.CASCADE, related_name='results')
    lower_limit = models.PositiveIntegerField()
    upper_limit = models.PositiveIntegerField()
    text = models.TextField()

    def __str__(self):
        return self.text