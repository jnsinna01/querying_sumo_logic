from django.forms import ModelForm, TextInput
from .models import SumoLogic


class SumoLogicForm(ModelForm):
    class Meta:
        model = SumoLogic
        fields = ['Query', 'From_Date_Time', 'To_Date_Time']
        widgets = {'Query': TextInput(attrs={'class': 'input', 'placeholder': 'Query name'}),
                   'From_Date_Time': TextInput(attrs={'class': 'input', 'placeholder': 'Start Date'}),
                   'To_Date_Time': TextInput(attrs={'class': 'input', 'placeholder': 'End Date'})}
