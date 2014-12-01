from django.shortcuts import render
from accounts.forms import CreateUserForm
from django.http import HttpResponseRedirect
 
from django.views.generic.edit import FormView

class RegisterView(FormView):
    form_class = CreateUserForm
    template_name = 'accounts/register.html'
    success_url = '/'
    
    def form_valid(self,form):
        form.save()
        #form.send_email()
        return super(RegisterView, self).form_valid(form)

def register(request):
    form = CreateUserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
      
    return render(request, "accounts/register.html",{"form": form})