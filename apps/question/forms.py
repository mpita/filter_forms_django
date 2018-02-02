from django import forms
from .models import Answer, Question


class AnswerForm(forms.ModelForm):
    question = forms.ModelChoiceField(
        label='Pregunta',
        queryset=Question.objects.none(),
        widget=forms.Select(
            attrs={
                'id': 'id_question'
            }
        ),
        empty_label='seleccione una pregunta'
    )
    answer = forms.CharField(
        label='Respuesta',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Escriba su respuesta',
            }
        ),
        max_length=1000
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        try:
            self.base_fields['question'].queryset = Question.objects.filter(user=user)
        except Exception:
            pass
        super(AnswerForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Answer
        fields = ('question', 'answer')
