from django import forms
from django.forms import fields
from Librariesapp.models import auth_user, books


USER_TYPE_CHOICES = (
 ('Admin', '1'),
('student', '2'))

class auth_userforms(forms.ModelForm):
    user_type = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=USER_TYPE_CHOICES)

    class Meta:
        model=auth_user

        fields=['user_type']



class bookforms(forms.ModelForm):
    class Meta:
        model=books
        fields="__all__"