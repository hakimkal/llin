from django import forms as form
from django.template import Context
from django.template.loader  import get_template

from django.core.mail import EmailMessage

class ContactForm(form.Form):
    email = form.EmailField()
    name = form.CharField()
    subject = form.CharField()
    message = form.CharField( widget=form.Textarea)
    
    
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        email = self.cleaned_data["email"]
        subject  = self.cleaned_data["subject"]
        message = self.cleaned_data["message"]
        name  = self.cleaned_data["name"]
        to = ['olusholadabiri@yahoo.com']
       
        cc_list = ['info@leproghrammeen.com']
        from_email = email
        ctx = {'email':email, 'message':message, 'name': name, 'subject':subject}
        message = get_template('states/email.html').render(Context(ctx))
        msg = EmailMessage(subject,message, to=to, from_email=from_email,cc=cc_list,  headers = {'Reply-To': email })
        msg.content_subtype = 'html'
        if msg.send():
            return True
        else:
            return False 
        