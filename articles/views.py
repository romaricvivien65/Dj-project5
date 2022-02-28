from django.http.request import HttpHeaders
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from . import models
from .forms import Form_articles

def view_articles(request):
  data_articles = models.Mdl_articles.objects.all().order_by('-date_publication')
  return render(request, 'articles/liste.html', context={'tpl_articles':data_articles})


def view_article(request, slug):
    data_article = get_object_or_404(models.Mdl_articles, slug=slug)
    return render(request, 'articles/detail.html', context={'tpl_article':data_article})

  # try:
  #   data_article = models.Mdl_articles.objects.get(slug=slug)
  #   return render(request, 'articles/detail.html', context={'tpl_article':data_article})
  # except models.Mdl_articles.DoesNotExist:
  #   raise Http404("L'article n'existe pas")
def view_creer(request):
  
  if request.method == 'POST':
    data_form = Form_articles(request.POST)
    data_form.save()
    return HttpResponseRedirect(reverse('app_articles:link_articles'))
    # return HttpResponseRedirect('/articles/')
  else:
    data_form = Form_articles()
    return render(request, 'articles/creer.html', context = {'tpl_form': data_form})