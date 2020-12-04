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