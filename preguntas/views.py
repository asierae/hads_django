from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Question, Choice,Jugador,Historico
from .forms import QuestionForm,ChoiceForm,JugadorForm
import random
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):
	template_name = 'preguntas/index.html'
	context_object_name = 'latest_question_list'
	def get_queryset(self):
		return Question.objects.all()

def question_list(request):
    questions = Question.public.all()
    context = {'questions': questions}
    return render(request, 'preguntas/detail.html', questions)
class DetailView(generic.DetailView):
    model = Question
    template_name = 'preguntas/detail.html'
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'preguntas/results.html'
class PlayView(generic.DetailView):
    template_name = 'preguntas/play.html'
    context_object_name = 'random_question'
    def get_object(self):
        question_id=random.randrange(Question.objects.count())+1
        return get_object_or_404(Question, pk=question_id)

def playquiz(request):
    if request.method == 'POST':
        tema = request.POST.get('topic','')
        if len(tema)>0:
            questions=Question.objects.filter(topic=tema)
            return render(request, 'preguntas/playquiz.html',{'questions':questions,})
        else:
            topics=Question.objects.all().order_by().values_list('topic',flat=True).distinct()
            return render(request, 'preguntas/playquiz.html',{'topics':topics,})
    else:
        topics=Question.objects.all().order_by().values_list('topic',flat=True).distinct()
        return render(request, 'preguntas/playquiz.html',{'topics':topics,})
def playquiztopic(request,topic):
    question=Question.objects.filter(topic=topic)[:1].get()
    return render(request, 'preguntas/playquiz.html',{'question':question,})


def getNextQuestion(request):
    topic = request.GET.get('topic', None)
    n = int(request.GET.get('n', None))
    if n<Question.objects.filter(topic=topic).count():
        question=Question.objects.filter(topic=topic)[n]
        if question.imagen:
            imagen=question.imagen.url
        else:
            imagen='no'
        data = {'q': question.question_text,
                'c1': question.c1,
                'c2': question.c2,
                'c3': question.c3,
                'correct': question.correct,
                'img': imagen,
        }
        return JsonResponse(data)
    else:
        data={'msj':'fin'}
        return JsonResponse(data)
def historial(request):
    a = request.GET.get('a', None)
    f = request.GET.get('f', None)
    j = Jugador.objects.filter(nick=request.session['nick']).get()
    h=Historico.objects.create(aciertos=a,fallos=f,jugador=j)
    h.save()
    data = {'msj':'Registrado!'
        }
    return JsonResponse(data)

def getHistorial(request):
    historial=Historico.objects.filter(jugador=j)
    return render(request, 'preguntas/verHistorico.html',{'his':historial,})
@login_required
def add(request):
    template_name = 'preguntas/add.html'
    context_object_name = 'num_preg'
    myquestions=Question.objects.filter(user=request.user.id)
    return render(request, 'preguntas/add.html',{'myquestions':myquestions,})

def empezarjuego(request):
    if request.method == 'POST':
        jugador=request.POST.get('nick','')
        tmp=Jugador.objects.filter(nick=jugador)
        request.session['nick']=jugador
        if not tmp:
            j = Jugador(nick=jugador)
            j.save()
        topics=Question.objects.all().order_by().values_list('topic',flat=True).distinct()
        return render(request, 'preguntas/playquiz.html',{'topics':topics,})
    else:
        form = JugadorForm()
        context = {'form': form}
        return render(request, 'preguntas/empezarjuego.html', context)

@login_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST,request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            form.save_m2m()

            myquestions=Question.objects.filter(user=request.user.id)
            return render(request, 'preguntas/add.html',{'myquestions':myquestions,})
    else:
        form = QuestionForm()
        context = {'form': form}
        return render(request, 'preguntas/addquestion.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'preguntas/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('preguntas:results', args=(question.id,)))