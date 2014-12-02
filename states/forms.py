from django import forms as form

class ContactForm(form.Form):
    email = form.EmailField()
    name = form.CharField()
    subject = form.CharField()
    message = form.CharField( widget=form.Textarea)
    
    
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass