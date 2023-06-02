from django import forms
from django.forms.models import ModelForm
from .models import Post
from django.core.exceptions import ValidationError


class CreateForm(ModelForm):
    class Meta:
        model =  Post
        fields = ['category', 'user', 'title' , 'description' , 'image']
        widgets = {
            'category':forms.Select(attrs={'class' : 'form-control'}),
            'user':forms.Select(attrs={'class' : 'form-control'}),
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'description': forms.Textarea(attrs={'class' : 'form-control'}),
            
        }


            
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if '<javascript>' in title:
    #         x = title.replace('m' , 'hahahah ')
    #         raise ValidationError('no hahahah ..... ' , x)
    #     return title  