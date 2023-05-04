from django import forms
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['topic_name']

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=['name','url']

class Access_RecordForm(forms.ModelForm):
    class Meta:
        model=Access_Records
        fields=['author','date']