from django.shortcuts import render
from .forms import NewsUserForm
from . models import NewsUsers

def newsletter_subscribe(request):
  if request.method == 'POST':
    form = NewsUserForm(request.POST)
    if form.is_valid():
      instance = form.save()
      print('your email is already added to our database')
  else:
    form = NewsUserForm()
  context = {'form':form}
  template = "newsletter/subscribe.html"
  return render(request, template, context)




