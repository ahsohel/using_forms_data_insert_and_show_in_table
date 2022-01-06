from django.forms import ModelForm
from . models import form_models

class my_first_form(ModelForm):
    class Meta:
        model = form_models
        # fields = ['name', 'phone']            #or necar ta lekhla sob gola show hoba
        # exclude = ['name']            #ae mane name cara bake gola nea form banabe
        fields = '__all__'