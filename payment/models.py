from django.db import models
from django.contrib.auth.models import User
import datetime

from django.utils import timezone




class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance_rub = models.IntegerField(max_length=50, default=0)
    balance_dol = models.IntegerField(max_length=50, default=0)
    balance_eur = models.IntegerField(max_length=50, default=0)
    def __str__(self):
        return 'На вашем рублевом счете {} руб\
        На вашем валютном счете {} USD' \
        'На вашеем валютном счете {} EUR'.format\
            (self.balance_rub,self.balance_dol, self.balance_eur)

class Credit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    credit = models.IntegerField(max_length=50,default=0)
    name_credit = models.CharField(max_length=50)
    def __str__(self):
        return 'Кредит за {}. Осталось погасить {} '.\
            format(self.name_credit, self.credit)


class Money(models.Model):
    usd = models.DecimalField(max_digits=5, decimal_places=2, default=01.00)
    usd_sale = models.DecimalField(max_digits=5, decimal_places=2, default=01.00,name='USD Продажа банком')
    usd_buy = models.DecimalField(max_digits=5, decimal_places=2, default=01.00,name='USD Покупка банком')
    eur = models.DecimalField(max_digits=5, decimal_places=2, default=01.00)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return 'Котировка валют на сегодня'

class Currency():
    pass
