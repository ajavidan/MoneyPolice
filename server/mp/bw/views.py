
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response


from .models import Transaction
from .models import Payer
from .models import Fund
from .models import Budget

from .serializers import PayerSerializer
from .serializers import TransactionSerializer
from .serializers import FundDetailSerializer
from .serializers import FundSummarySerializer
from .serializers import BudgetSerializer

import datetime

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request):
        f = Fund.objects.get(id=request.data['fund_id'])
        p = Payer.objects.get(id=request.data['payer_id'])
        t = Transaction(fund=f, payer=p, amount=request.data['amount'])
        f.amount = f.amount + t.amount
        f.save()
        t.save()
        return Response({"transaction_id": t.id, "fund_amount": f.amount}, status=status.HTTP_201_CREATED)

class FundViewSet(viewsets.ModelViewSet):
    queryset = Fund.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return FundDetailSerializer
        elif self.action == 'retrieve':
            return FundDetailSerializer
        else:
            return FundSummarySerializer

    def list(self, request):
        serializer_class = FundDetailSerializer
        return super(FundViewSet, self).list(request)

    def create(self, request):
        b = Budget.objects.get(id=request.data['budget_id'])
        f = Fund(name=request.data['name'], amount=0, budget=b,
                    f_type=request.data['f_type'], limit=request.data['limit'])
        f.save()
        print(b.fund_set)
        return Response({"fund_id":f.id}, status=status.HTTP_201_CREATED)

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def create(self, request):
        b = Budget(name=request.data['name'])
        b.save()
        return Response({"budget_id": b.id}, status=status.HTTP_201_CREATED)

class PayerViewSet(viewsets.ModelViewSet):
    queryset = Payer.objects.all()
    serializer_class = PayerSerializer

    def create(self, request):
        b = Budget.objects.get(id=request.data['budget_id'])
        p = Payer(name=request.data['name'], budget=b)
        p.save()
        return Response({"payer_id": p.id}, status=status.HTTP_201_CREATED)

    # @detail_route(methods=['post'])
    # def new_payer(self, request):
    #     serializer = PayerSerializer(data=request.data)
    #     if serializer.is_valid():
    #         p = serializer.save()
    #         b = Budget.objects.get(id=request.data['budget_id'])
    #         p.budget = b
    #         p.save()
    #         return Response({'payer created: %i' % p.id})
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)
    #



def index(request):

    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)
    budget = Budget.objects.get(name="Tylers Budget")

    context = {
        'budget': budget,
    }
    template = loader.get_template('bw/index.html')
    return HttpResponse(template.render(context, request))


# def new_budget(request):


def view_budget(request):
    budget = Budget.objects.get(name="Tylers Budget")


def recent_transactions(request):

    if (request.content_type == 'text/plain'):
        return HttpResponse("HTML response")
    elif (request.content_type == 'application/json'):
        return HttpResponse("REST response")

    now = datetime.datetime.now()

    return HttpResponse(" ContentType: %s Recent Transactions for %d/%d" % (request.content_type, now.month, now.year))

def new_transaction(request):
        # Get POST data
        # Create new model with data
        # submit model to db
        #TODO: add rest option
    # render new_transaction tempatnsactione

    return render(request, 'bw/transactions/new.html')

def recent_by_category(request, category):
    return HttpResponse("Recent transaction category %s" % category)

def recent_by_type(request, t_type):

    # trans = Transaction.all()
    #Get recent (this month) Transactions for the requested type
    # render transaction_list template with smaller list

    t_type_name = 'spending'
    if (t_type == '0'):
        t_type_name = 'saving'

    return HttpResponse("Recent transaction type %s" % t_type_name)

def recent_by_payer(request, payer):

    # Get recent (this month) Transactions for requested payer

    # render transaction_list template with smaller list
    return HttpResponse("Recent transaction payer %s" % payer)

def transactions(request):

    return HttpResponse("All transactions")
    # render all transactions
