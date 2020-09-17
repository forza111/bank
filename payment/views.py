from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader

from .models import User,Balance,Credit

'''def index(request):
    latest_user_list = User.objects.all()
    template = loader.get_template('payment/index.html')
    context = {'latest_user_list': latest_user_list,}
    return HttpResponse(template.render(context, request))'''
class IndexView(generic.ListView):
    template_name = 'payment/index.html'
    context_object_name = 'latest_user_list'
    def get_queryset(self):
        return User.objects.all()

class DetailView(generic.DetailView):
    model = Balance
    template_name = 'payment/detail.html'


