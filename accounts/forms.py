from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta():
        model = User
        
        fields = ('email','first_name','username', 'last_name','password1','password2',)
    def send_email(self):
       # send email using the self.cleaned_data dictionary
       pass   
    
    def save(self, commit=True):
        user = super(CreateUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_active = True
        if commit:
            user.save()
        return user
        