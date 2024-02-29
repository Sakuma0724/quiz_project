from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import Question

def title_page(request):
    return render(request, 'quiz/title_page.html')

def quiz_page(request, question_id):
    question = Question.objects.get(pk=question_id)
    choices = question.choice_set.all()
    correct_answers = question.correct_choices.all()
    user_answers = []
    feedback = None
    next_question = None

    if request.method == 'POST':
        selected_choice_ids = request.POST.getlist('choices')
        if selected_choice_ids:
            user_answers = question.choice_set.filter(pk__in=selected_choice_ids)
            if set(user_answers) == set(correct_answers):
                feedback = "正解◎"
                request.session.setdefault('correct_count', 0)
                request.session['correct_count'] += 1
            else:
                feedback = "不正解☓"

    next_question_id = question_id + 1
    try:
        next_question = Question.objects.get(pk=next_question_id)
    except Question.DoesNotExist:
        pass

    total_questions = Question.objects.count()
    correct_count = request.session.get('correct_count', 0)
    accuracy = (correct_count / total_questions) * 100 if total_questions > 0 else 0

    return render(
        request,
        'quiz/quiz_page.html',
        {
            'question': question,
            'choices': choices,
            'user_answers': user_answers,
            'feedback': feedback,
            'next_question': next_question,
            'correct_count': correct_count,
            'total_questions': total_questions,
            'accuracy': accuracy,
        }
    )

def quiz_start(request):
    request.session.pop('correct_count', None)
    return redirect('quiz_page', question_id=1)
