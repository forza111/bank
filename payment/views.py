from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse,Http404
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

def detail(requset, user_id):
    user = get_object_or_404(User, pk=user_id)
    check_credit = Credit.objects.filter(user = user).exists()
    credit = Credit.objects.filter(user = user)
    try:
        balance = Balance.objects.get(user = user)
    except(KeyError,Balance.DoesNotExist):
        return render(requset, 'payment/detail.html',
                      {
                          'user' : user,
                          'error_message': '{} not balance'.format(user),
                          'credit':credit,
                          'check_credit':check_credit
                      }
                      )
    else:
        return render(requset, 'payment/detail.html',
                      {'user': user, 'balance' : balance,'credit':credit,
                      'check_credit':check_credit} )


'''def detail(reqest, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404('No NO Noo')
    return render(reqest, 'payment/detail.html', {'user' : user})'''