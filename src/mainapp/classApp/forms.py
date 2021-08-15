from django.forms import ModelForm
from .models import djangoClasses

class ClassForm(ModelForm):
    class Meta:
        model = djangoClasses
        fields = '__all__'\
