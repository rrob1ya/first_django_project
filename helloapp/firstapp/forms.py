from unittest import result
from django import forms
 
class UserForm(forms.Form):
    field1 = forms.IntegerField()
    field2 = forms.IntegerField()

    