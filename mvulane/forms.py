from django.forms import ModelForm
from django import forms
from .models import Clients

class ClientsForm(ModelForm):

        def __init__(self, *args, **kwargs):
            super(ClientsForm, self).__init__(*args, **kwargs)

        class Meta:
            model = Clients

            fields = '__all__'
            widgets = {
                       'name': forms.TextInput(attrs={'class':'form-control',}),
                       'email': forms.TextInput(attrs={'class':'form-control',}),
                       'message': forms.TextInput(attrs={'class':'form-control',}),

                       }
