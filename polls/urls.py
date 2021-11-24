#The path imports some module that allows django to find the views and other files in the current or another directory
from django.urls import path

#This imports views fromt the current path, hence the .
from . import views

app_name = 'polls'

#This is where we tell django where to go?
urlpatterns = [
    path('', views.index, name='index'),
     # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('create/', views.create, name = 'create' )
]