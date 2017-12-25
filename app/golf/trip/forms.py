from django import forms
from ..models import Trip

class CreateForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ('teams',)

class TeamAddForm(forms.Form):
    def __init__(self, *args, **kwargs):
        queryset = kwargs.pop('queryset')
        super(TeamAddForm, self).__init__(*args, **kwargs)
        self.fields['teams'] = forms.ModelMultipleChoiceField(queryset)
