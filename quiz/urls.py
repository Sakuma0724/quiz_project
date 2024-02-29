from django.urls import path
from .views import title_page, quiz_page, quiz_start

urlpatterns = [
    path('title/', title_page, name='title_page'),  
    path('<int:question_id>/', quiz_page, name='quiz_page'),
    path('start/', quiz_start, name='quiz_start'),
]
