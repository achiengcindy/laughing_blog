from django.shortcuts import render
from django.contrib import messages

from .forms import NewsUserForm
from .models import NewsUsers
from .emails import send_multiple_email


def newsletter_subscribe(request):
  if request.method == 'POST':
    form = NewsUserForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)#we dont want to save just yet
      if NewsUsers.objects.filter(email=instance.email).exists():
        messages.warning(request, "your Email Already exists in our database")
      else:
        instance.save()
        messages.success(request, "your Email has been submitted to our database")
        #send_mail('Laughing blog tutorial series','welcome','mail@achiengcindy.com',['instance.email'], fail_silently=False)
        send_multiple_email('name', 'email')
        
  else:
    form = NewsUserForm()
  context = {'form':form}
  template = "newsletter/subscribe.html"
  return render(request, template, context)


