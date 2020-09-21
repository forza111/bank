from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader

from .models import User,Balance,Credit

class IndexView(generic.ListView):
    '''Shows userlist'''
    template_name = 'payment/index.html'
    context_object_name = 'latest_user_list'
    def get_queryset(self):
        return User.objects.all()

def detail(requset, user_id):
    '''
    Shows information about user balance and credit balance.
    check_credit test the user has a credit and output  True or False'''
    user = get_object_or_404(User, pk=user_id)
    check_credit = Credit.objects.filter(user = user).exists()
    try:
        balance = Balance.objects.get(user = user)
    except(KeyError,Balance.DoesNotExist):
        return render(requset, 'payment/detail.html',
                      {
                          'user' : user,
                          'error_message': 'У пользователя {} нет открытого счета в банке'.format(user),
                          'check_credit':check_credit
                      }
                      )
    else:
        return render(requset, 'payment/detail.html',
                      {'user': user,'balance' : balance,
                      'check_credit':check_credit} )
def credit_repayment(requset, user_id):
    user = get_object_or_404(User, pk=user_id)
    check_credit = Credit.objects.filter(user = user).exists()
    return render(requset, 'payment/credit_repayment.html',
                  {'user': user,
                   'check_credit': check_credit})
