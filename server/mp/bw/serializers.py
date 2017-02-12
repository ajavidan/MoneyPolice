from rest_framework import serializers

from .models import Transaction
from .models import Fund
from .models import Budget
from .models import Payer

class TransactionSerializer(serializers.ModelSerializer):
    payer_name = serializers.StringRelatedField(source='payer.name')
    fund_name = serializers.StringRelatedField(source='fund.name')
    class Meta:
        model = Transaction
        fields = ('amount', 'payer_name', 'time', 'fund_name')

class FundSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = ('name', 'amount','f_type', 'limit')

class FundDetailSerializer(serializers.ModelSerializer):
    budget_name = serializers.StringRelatedField(source='budget.name')
    transaction_set = TransactionSerializer(many=True)
    class Meta:
        model = Fund
        fields = ('name', 'id', 'amount', 'limit', 'f_type', 'budget_name', 'transaction_set')

class PayerSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Payer
        fields = ('name',)

class PayerSerializer(serializers.ModelSerializer):
    budget_name = serializers.StringRelatedField(source='budget.name')
    # budget = BudgetSerializer(
    # budget = serializers.PrimaryKeyRelatedField(queryset=Bdget.objects.all())
    class Meta:
        model = Payer
        fields = ('name', 'id', 'budget_name')

    def create(self, validated_data):
        print(validated_data)
        return Payer(name=validated_data['name'])
        # budget = Budget.objects.get(id=validated_data['budget']



class BudgetSerializer(serializers.ModelSerializer):
    fund_set = FundSummarySerializer(many=True)
    payer_set = PayerSummarySerializer(many=True)
    class Meta:
        model = Budget
        fields = ('name', 'id', 'fund_set', 'payer_set')
