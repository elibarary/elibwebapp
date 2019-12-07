from django import forms
from .models import FeedBack

class FeedCreateForm(forms.ModelForm):
    name = forms.CharField(label='username')
    email= forms.EmailField(label='email')
    body = forms.CharField(label='type here|اكتب اقتراحك هنا', widget=forms.Textarea)

    class Meta:
        model = FeedBack
        fields = ['name', 'email','body']