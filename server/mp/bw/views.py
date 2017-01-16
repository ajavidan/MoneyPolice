from django.shortcuts import render
from django.http import HttpResponse

from .models import Transaction
import datetime
# Create your views here.

def index(request):

    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)
    return render(request, 'bw/index.html')

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

    return HttpResponse("Create a new transatcion")

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
