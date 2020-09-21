from django.urls import path
from . import views

app_name = 'payment'
urlpatterns=[
    path('', views.IndexView.as_view(),name = 'index'),
    path('<int:user_id>/', views.detail,name = 'detail'),
    path('<int:user_id>/credit_repayment', views.credit_repayment,
         name='credit_repayment'),
]
