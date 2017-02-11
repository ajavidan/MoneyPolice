package com.software.btc.moneypolice;

/**
 * Created by blair.javidan on 2/11/2017.
 */

public class Fund {
    private String name;
    private int fund_id;
    private int limit;
    private int amount;
    private int usedAmount;

    public Fund(String name, int amount) {
        this.name = name;
        this.fund_id = getFundIdByFundName(name);
        this.amount = amount;
    }

    private int getFundIdByFundName(String name) {
        switch (name){
            case "Food":
                return 1;
            case "Grocery":
                return 2;
            default:
                return -1;
        }
    }

    public int getLimit() {
        return limit;
    }

    public void setLimit(int limit) {
        this.limit = limit;
    }

    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public int getUsedAmount() {
        return usedAmount;
    }

    public void setUsedAmount(int usedAmount) {
        this.usedAmount = usedAmount;
    }

    public int getFund_id() {
        return fund_id;
    }

    public void setFund_id(int fund_id) {
        this.fund_id = fund_id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
