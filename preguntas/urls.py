from django.conf.urls import url

from . import views


app_name = 'preguntas'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'play/$', views.PlayView.as_view(), name='play'),
    url(r'add/$', views.add, name='add'),
    url(r'playquiz/$', views.playquiz, name='playquiz'),
    url(r'^playquiz/(?P<topic>[\w\-]+)/$',views.playquiztopic, name='playquiztopic'),
    url(r'^create/$', views.create_question,name='create_question'),
    url(r'^empezarjuego/$', views.empezarjuego,name='empezarjuego'),
    url(r'^next/$', views.getNextQuestion,name='getNextQuestion'),
    url(r'^stadistics/$', views.historial,name='historial'),
]