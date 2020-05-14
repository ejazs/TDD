from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Note
from django.http import HttpResponseRedirect
# Create your views here.

class Home(View):
    
    def get(self, request):
        # context = {"title":request.POST.get('text_item')}
        notes = Note.objects.all()
        context = {'notes': notes}
        return render(request, 'home.html', context)
    
    def post(self, request):
        # print()
        Note.objects.create(title= request.POST.get('text_item'))
        return HttpResponseRedirect('/')

