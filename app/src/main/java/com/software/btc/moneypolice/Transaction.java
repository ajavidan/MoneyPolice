package com.software.btc.moneypolice;

import java.util.Date;

/**
 * Created by blair.javidan on 2/11/2017.
 */

public class Transaction {
    private int amount;
    private int fund_id;
    private int payer_id;
    private String time;


    public Transaction(Fund fund, int payer_id) {
        this.amount = fund.getAmount();
        this.fund_id = fund.getFund_id();
        this.payer_id = payer_id;
        this.time = new Date().toString();
    }

    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public int getFund_id() {
        return fund_id;
    }

    public void setFund_id(int fund_id) {
        this.fund_id = fund_id;
    }

    public int getPayer_id() {
        return payer_id;
    }

    public void setPayer_id(int payer_id) {
        this.payer_id = payer_id;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public String toJsonString(){
        return JsonUtil.getTransactionJson(this);
    }
}
