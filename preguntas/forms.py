from django.forms import ModelForm

from .models import Question,Choice,Jugador


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('user', 'date_created', 'date_updated')
class ChoiceForm(ModelForm):
	class Meta:
		model=Choice
		exclude = ('date_created', 'date_updated','question')
class JugadorForm(ModelForm):
	class Meta:
		model=Jugador
		exclude=('date_updated',)