from django import forms
from app.models import *

class SchoolForm(forms.Form):
    Sname=forms.CharField()
    Sprincipal=forms.CharField()
    Slocation=forms.CharField()

class WebForm (forms.Form):
    tl=[[to.Sname,to.Sname] for to in School.objects.all()]
    
