from django.urls import path
from . import views

app_name = 'payment'
urlpatterns=[
    path('', views.IndexView.as_view(),name = 'index'),
    path('<int:user_id>/', views.detail,name = 'detail'),
    path('<int:user_id>/credit_repayment', views.credit_repayment,
         name='credit_repayment'),
    path('about', views.about, name='about'),
    path('<int:user_id>/sale_buy', views.sale_buy, name='sale_buy'),
    path('<int:user_id>/change_sale_buy', views.change_sale_buy, name='change_sale_buy'),

]
