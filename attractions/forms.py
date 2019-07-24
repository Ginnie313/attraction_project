from django.forms import ModelForm
from attractions.models import Attraction
class AttractionForm(ModelForm):
    class Meta:
        model = Attraction
        exclude = ['tags', 'notes']
