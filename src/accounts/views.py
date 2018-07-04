from django.shortcuts import render , redirect
from .forms import SignupForm


def register(request):
  if request.method == 'POST':
    userform = SignupForm(request.POST)
    if userform.is_valid():
    	userform.save()
    	return redirect('login')
   
  else:
    userform = SignupForm()

  context = {'userform':userform}
  template = "accounts/signup.html"
  return render(request, template, context)


