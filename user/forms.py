from django import forms
from . import models
class LoginForm(forms.Form):
    username=forms.CharField(label='name',max_length=10)
    password=forms.CharField(label='password',widget=forms.PasswordInput())

class DateInput(forms.DateInput):
    input_type = 'date'

class DiaryForm(forms.ModelForm):
    class Meta:
        model=models.Diary
        fields=['note','ddate',]
        widgets={
            'ddate':DateInput(),
        }


class ContactForm(forms.Form):
    CITY=[
        ['Sh','Shanghai'],
        ['Bj','Beijing'],
    ]
    user_name=forms.CharField(max_length=10,initial='nick')
    user_city=forms.ChoiceField(choices=CITY)
    user_school=forms.BooleanField(required=False)
    user_email=forms.EmailField()
    user_message=forms.CharField(widget=forms.Textarea)
