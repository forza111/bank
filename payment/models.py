from django.db import models
import datetime

from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    age = models.DateTimeField('Date of birth')
    phone = models.CharField(max_length=16)

    def __str__(self):
        return self.username


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
