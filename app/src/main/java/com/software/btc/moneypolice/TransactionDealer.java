package com.software.btc.moneypolice;

import android.widget.RemoteViews;

/**
 * Created by blair.javidan on 2/11/2017.
 */

public class TransactionDealer {

    private RemoteViews view;
    private Transaction transaction;


    public TransactionDealer(RemoteViews view, Transaction transaction) {
        this.view = view;
        this.transaction = transaction;
    }

    public RemoteViews getView() {
        return view;
    }

    public void setView(RemoteViews view) {
        this.view = view;
    }

    public Transaction getTransaction() {
        return transaction;
    }

    public void setTransaction(Transaction transaction) {
        this.transaction = transaction;
    }

    public void sendTransaction(String url){
        HttpRequestTask httpRequestTask = new HttpRequestTask(){
            @Override
            protected void onPostExecute(String s) {
                super.onPostExecute(s);
                System.out.println(s);
                //Set views
            }
        };
    }
}
