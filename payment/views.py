from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader

from .models import User,Balance,Credit,Money

class IndexView(generic.ListView):
    '''Shows userlist'''
    template_name = 'payment/index.html'
    context_object_name = 'latest_user_list'
    def get_queryset(self):
        return User.objects.all()

def detail(request, user_id):
    '''
    Shows information about user balance and credit balance.
    check_credit test the user has a credit and output  True or False'''
    user = get_object_or_404(User, pk=user_id)
    check_credit = Credit.objects.filter(user = user).exists()
    try:
        balance = Balance.objects.get(user = user)
    except(KeyError,Balance.DoesNotExist):
        return render(request, 'payment/detail.html',
                      {
                          'user' : user,
                          'error_message': 'У пользователя {} нет открытого счета в банке'.format(user),
                          'check_credit':check_credit,
                          'last_currency': Money.objects.latest('pub_date')
                      }
                      )
    else:
        return render(request, 'payment/detail.html',
                      {'user': user,'balance' : balance,
                      'check_credit':check_credit,
                       'last_currency':Money.objects.latest('pub_date')} )
def credit_repayment(request, user_id, credit_id):
    user = get_object_or_404(User, pk=user_id)
    credit = get_object_or_404(Credit, user=user, pk=credit_id)

    check_credit = Credit.objects.filter(user = user).exists()
    return render(request, 'payment/credit_repayment.html',
                  {'user': user,
                   'check_credit': check_credit,
                   'credit' : credit
                   })
def about(request):
    about_us = 'Данное приложение разработано на фреймворке Django. ' \
               'Для более подробной информацией по поводу использования данного приложения обращайтесь по адресу' \
               ' https://github.com/forza111/bank'

    return render(request,'payment/about.html', {'about_us': about_us})

'''def money(request):
    last_currency = Money.objects.latest('pub_date')
    return render(request, 'payment/about.html', {'last_currency': last_currency})'''

def sale_dol(request,user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'payment/sale_dol.html', {
        'user': user,
    }
                  )

def change_sale_dol(request,user_id):
    user = get_object_or_404(User, pk=user_id)
    last_currency = Money.objects.latest('pub_date')
    try:
        balance = Balance.objects.get(user=user)
    except(KeyError, Balance.DoesNotExist):
        return render(request, 'payment/sale_dol.html',
                      {
                          'user': user,
                          'error_message': 'У пользователя {} нет открытого счета в банке'.format(user)
                      }
                      )
    else:
        if int(request.POST['balance_dol']) > balance.balance_dol:
            return render(request, 'payment/sale_dol.html',
                            {'user': user, 'error_message ': 'Недостаточно средств'})
        else:
            balance.balance_dol = balance.balance_dol - int(request.POST['balance_dol'])
            balance.balance_rub = balance.balance_rub + (int(request.POST['balance_dol'])*last_currency.usd)
            balance.save()
            return HttpResponseRedirect(reverse('payment:detail', args=(user.id,)))

def sale_eur(request,user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'payment/sale_eur.html', {
        'user': user,
    }
                  )

def change_sale_eur(request,user_id):
    user = get_object_or_404(User, pk=user_id)
    last_currency = Money.objects.latest('pub_date')
    try:
        balance = Balance.objects.get(user=user)
    except(KeyError, Balance.DoesNotExist):
        return render(request, 'payment/sale_eur.html',
                      {
                          'user': user,
                          'error_message': 'У пользователя {} нет открытого счета в банке'.format(user)
                      }
                      )
    else:
        if int(request.POST['balance_eur']) > balance.balance_eur:
            return render(request, 'payment/sale_eur.html',
                            {'user': user, 'error_message ': 'Недостаточно средств'})
        else:
            balance.balance_eur = balance.balance_eur - int(request.POST['balance_eur'])
            balance.balance_rub = balance.balance_rub + (int(request.POST['balance_eur'])*last_currency.eur)
            balance.save()
            return HttpResponseRedirect(reverse('payment:detail', args=(user.id,)))

def change_credit_repayment(request,user_id,credit_id):
    user = get_object_or_404(User, pk=user_id)
    credit = get_object_or_404(Credit, user=user, pk=credit_id)
    balance = Balance.objects.get(user=user)

    if int(request.POST['repayment_rub']) > balance.balance_rub:
        return render(request, 'payment/credit_repayment.html',
                      {
                        'user': user,
                       'credit':credit,
                       'error_message ': 'Недостаточно средств'
                       })
    else:
        balance.balance_rub = balance.balance_rub - (int(request.POST['repayment_rub']))
        balance.save()
        credit.credit = credit.credit - (int(request.POST['repayment_rub']))
        credit.save()
        return HttpResponseRedirect(reverse('payment:detail', args=(user.id,)))



