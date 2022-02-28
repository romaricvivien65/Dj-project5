from django.db import models

class Mdl_articles(models.Model):
  titre = models.CharField(max_length=150)
  contenu = models.TextField()
  date_publication = models.DateTimeField(auto_now_add=True)
  slug = models.SlugField(max_length=100)
  image = models.ImageField(default='default.jpg')

  def __str__(self):
    return self.titre

