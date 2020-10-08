from django.urls import path
from . import views

app_name = 'payment'
urlpatterns=[
    path('', views.IndexView.as_view(),name = 'index'),
    path('<int:user_id>/', views.detail,name = 'detail'),
    path('<int:user_id>/credit_repayment/<int:credit_id>', views.credit_repayment,
         name='credit_repayment'),
    path('about', views.about, name='about'),
    path('<int:user_id>/sale_dol', views.sale_dol, name='sale_dol'),
    path('<int:user_id>/sale_eur', views.sale_eur, name='sale_eur'),
    path('<int:user_id>/change_sale_dol', views.change_sale_dol, name='change_sale_dol'),
    path('<int:user_id>/change_sale_eur', views.change_sale_eur, name='change_sale_eur'),
    path('<int:user_id>/change_credit_repayment/<int:credit_id>', views.change_credit_repayment,
         name='change_credit_repayment'),
]
