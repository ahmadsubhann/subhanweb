# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import kategori,produk

def members(request):
  template = loader.get_template('menu.html')
  return HttpResponse(template.render())

def kategori_produk(request):
  data = kategori.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'contoh': 'ini variabel',
    'contoh': 'ini contoh lagi',
    'kategori': data,
  }
  return HttpResponse(template.render (context, request))