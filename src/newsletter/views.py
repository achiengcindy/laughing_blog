from django.shortcuts import render
from .forms import NewsUserForm
from . models import NewsUsers

def newsletter_subscribe(request):
  if request.method == 'POST':
    form = NewsUserForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      if NewsUsers.objects.filter(email=instance.email).exists():
        print('your email Already exists in our database')
      else:
        instance.save()
        print('your email has been submitted to our database')
  else:
    form = NewsUserForm()
  context = {'form':form}
  template = "newsletter/subscribe.html"
  return render(request, template, context)


