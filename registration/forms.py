from django import forms

from .models import SimpleForm

class SimpleFormForm(forms.ModelForm):

    class Meta:
        model = SimpleForm
        fields = ('Vorname', 'Familienname','Telefonnummer')
