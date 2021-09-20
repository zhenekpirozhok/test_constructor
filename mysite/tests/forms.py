from django import forms
from .models import *


class CreateTestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = ['name', 'is_private', 'category', 'description', 'image']
        labels = {'name': 'Название',
                  'is_private': 'Приватность',
                  'category': 'Категория',
                  'description': 'Описание',
                  'image': 'Загрузить изображение',
                   }


class CreateQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['text', 'type']
        labels = {'text': 'Вопрос',
                  'type': 'Тип ответа на вопрос'}


class CreateAnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['text', 'value', 'image']
        labels = {'text': 'Ответ', 'value': 'Кол-во баллов', 'image': 'Загрузить изображение'}


class CreateResultForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = ['lower_limit', 'upper_limit', 'text']
        labels = {'lower_limit': 'Нижний порог (включительно)',
                  'upper_limit': 'Верхний порог (не включительно)',
                  'text': 'Текст результата'}
