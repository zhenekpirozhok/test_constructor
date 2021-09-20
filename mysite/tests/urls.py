from django.urls import path
from .views import *

urlpatterns = [
    path('', main_window, name='tests'),
    path('my_tests/', my_tests, name='my_tests'),
    path('my_tests/new/', new_test, name='new_test'),
    path('my_tests/<int:pk>/', test_detail, name='test_detail'),
    path('my_tests/<int:pk>/delete/', delete_test, name='delete_test'),
    path('my_tests/<int:pk>/pass/', pass_test, name='pass_test'),
    path('my_tests/<int:pk>/questions/', questions_list, name='questions_list'),
    path('my_tests/<int:pk>/questions/new/', new_question, name='new_question'),
    path('my_tests/<int:pk>/result/new/', new_result, name='new_result'),
    path('my_tests/<int:pk>/result/<int:result_pk>/delete/', delete_result, name='delete_result'),
    path('my_tests/<int:pk>/questions/<int:question_pk>/new/', new_answer, name='new_answer'),
    path('my_tests/<int:pk>/questions/<int:question_pk>/delete/', delete_question, name='delete_question'),
    path('my_tests/<int:pk>/questions/<int:question_pk>/<int:answer_pk>/delete/', delete_answer, name='delete_answer'),
    path('all_test/', all_tests, name='all_tests'),
    path('all_test/psychological/', ps_tests, name='ps_tests'),
    path('all_test/entertaining/', en_tests, name='en_tests'),
    path('all_test/educational/', ed_tests, name='ed_tests'),
]