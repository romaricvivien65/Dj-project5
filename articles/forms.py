from django.forms import ModelForm
from .models import Mdl_articles

class Form_articles(ModelForm):
  class Meta:
    model = Mdl_articles
    fields = ['titre', 'contenu', 'slug', 'image']
