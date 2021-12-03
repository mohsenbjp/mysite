from django import forms
from app1.models import Contact,Newsletter
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model=Contact
        fields='__all__'

        widgets = {
        'name':forms.TextInput(attrs={'placeholder':'Enter your name','class':'common-input mb-20 form-control','required':'','type':'text'}),
        'email':forms.EmailInput(attrs={'placeholder':'Enter email address','required':'','type':'email','class':"common-input mb-20 form-control"}),
        'subject':forms.TextInput(attrs={'placeholder':'Enter subject','type':'text','class':'common-input mb-20 form-control'}),
        'message':forms.Textarea(attrs={'class':'common-textarea form-control','name':'message', 'placeholder':'Enter Messege','required':'','rows':19})
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['subject'].required = False



class NewsletterForm(forms.ModelForm):
    class Meta:
        model=Newsletter
        fields='__all__'
