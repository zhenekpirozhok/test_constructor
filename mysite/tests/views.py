from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
import datetime
from .models import *
from .forms import *


def main_window(request):
    return render(request, 'main_window.html')


def my_tests(request):
    user = request.user.get_username()
    tests = Test.objects.filter(author=user).order_by('-published_date')
    return render(request, 'my_tests.html', {'tests': tests})


def new_test(request):
    if request.method == 'POST':
        form = CreateTestForm(request.POST, request.FILES)
        user = request.user.get_username()
        if form.is_valid():
            test = form.save()
            test.published_date = datetime.datetime.now()
            test.author = user
            test.save()
            return redirect('my_tests')
    else:
        form = CreateTestForm
    return render(request, 'new_test.html', {'form': form})


def test_detail(request, pk):
    test = get_object_or_404(Test, pk=pk)
    return render(request, 'test_detail.html', {'test': test})


def questions_list(request, pk):
    test = get_object_or_404(Test, pk=pk)
    return render(request, 'questions_list.html', {'test': test})


def new_question(request, pk):
    test = get_object_or_404(Test, pk=pk)
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.test = test
            question.save()
            return redirect('questions_list', pk=test.pk)
    else:
        form = CreateQuestionForm
    return render(request, 'new_question.html', {'form': form})


def new_answer(request, question_pk, pk):
    question = get_object_or_404(Question, pk=question_pk)
    if request.method == 'POST':
        form = CreateAnswerForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
        return redirect('questions_list', pk=pk)
    else:
        form = CreateAnswerForm
    return render(request, 'new_answer.html', {'form': form})


def pass_test(request, pk):
    test = get_object_or_404(Test, pk=pk)
    questions = test.questions.all()
    total_score = 0
    if request.method == 'POST':
        for question in questions:
            if question.type == 'S':
                name = question.create_label()
                try:
                    selected_answer = question.answers.get(pk=request.POST[name])
                except (KeyError, Answer.DoesNotExist):
                    return render(request, 'pass_test.html', {'test': test,
                                                              'error_message': "Вы не заполнили все поля."})
                else:
                    total_score += selected_answer.value
            elif question.type == 'M':
                for answer in question.answers.all():
                    try:
                        name = answer.create_label()
                    except (KeyError, Answer.DoesNotExist):
                        return render(request, 'pass_test.html', {'test': test,
                                                                  'error_message': "Вы не заполнили все поля."})
                    else:
                        if name in request.POST:
                            total_score += answer.value
        return render(request, 'result.html', {'total_score': total_score, 'test': test})
    else:
        return render(request, 'pass_test.html', {'test': test})


def delete_test(request, pk):
    test = get_object_or_404(Test, pk=pk)
    test.delete()
    return redirect('my_tests')


def delete_question(request, pk, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    question.delete()
    return redirect('questions_list', pk=pk)


def delete_answer(request, pk, question_pk, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk)
    answer.delete()
    return redirect('questions_list', pk=pk)


def all_tests(request):
    tests = Test.objects.filter(is_private=False).order_by('-published_date')
    return render(request, 'all_tests.html', {'tests': tests})


def ps_tests(request):
    tests = Test.objects.filter(is_private=False, category='PS').order_by('-published_date')
    return render(request, 'all_tests.html', {'tests': tests})


def ed_tests(request):
    tests = Test.objects.filter(is_private=False, category='EN').order_by('-published_date')
    return render(request, 'all_tests.html', {'tests': tests})


def en_tests(request):
    tests = Test.objects.filter(is_private=False, category='ED').order_by('-published_date')
    return render(request, 'all_tests.html', {'tests': tests})


def new_result(request, pk):
    test = get_object_or_404(Test, pk=pk)
    if request.method == 'POST':
        form = CreateResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.test = test
            result.save()
            return redirect('questions_list', pk=test.pk)
    else:
        form = CreateResultForm
    return render(request, 'new_result.html', {'form': form})


def delete_result(request, pk, result_pk):
    result = get_object_or_404(Result, pk=result_pk)
    result.delete()
    return redirect('questions_list', pk=pk)
