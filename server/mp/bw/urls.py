from django.conf.urls import url, include

from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'payers', views.PayerViewSet)
router.register(r'budgets', views.BudgetViewSet)
router.register(r'funds', views.FundViewSet)
router.register(r'transactions', views.TransactionViewSet)


urlpatterns = [

    url(r'^', include(router.urls)),
    # url(r'^transactions/recent/(?P<payer>[a-z]+)$', views.recent_by_payer, name='recent_by_payer'),
    # url(r'^transactions/recent/(?P<category>[A-Z]+)$', views.recent_by_category, name='recent_by_category'),
    # url(r'^transactions/recent/(?P<t_type>[01]+)$', views.recent_by_type, name='recent_by_type'),
    # url(r'^transactions/recent$', views.recent_transactions, name='recent_transactions'),
    # url(r'^transactions/all$', views.transactions, name='transactions'),
    # url(r'^transactions/new$', views.new_transaction, name='new_transaction'),
    url(r'^$', views.index, name='index')


]
