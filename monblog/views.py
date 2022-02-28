from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail

from .forms import Form_contact

def view_home(request):
  return render(request, 'index.html')

def view_contact(request):
  if request.method == "POST":
    data_form = Form_contact(request.POST)
    if data_form.is_valid():
      nom = data_form.cleaned_data['nom']
      prenom = data_form.cleaned_data['prenom']
      email = data_form.cleaned_data['email']
      message = data_form.cleaned_data['message']

      email_titre = f'Blog| {nom} {prenom} - {email}'
      send_mail(email_titre, message, 'biovacodev77@gmail.com',
      ['biovacodev77@gmail.com', 'viverebya@gmail.com'])
    
    return HttpResponseRedirect(reverse('link_remerciements'))
  else:
    data_form = Form_contact()
    return render(request, 'contact.html', {"tpl_form": data_form})

def view_remerciements(request):
  return HttpResponse("Merci de nous avoir contacter")
