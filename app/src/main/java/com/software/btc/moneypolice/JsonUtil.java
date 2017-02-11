package com.software.btc.moneypolice;

import com.google.gson.Gson;

/**
 * Created by blair.javidan on 2/11/2017.
 */

public class JsonUtil {

    private static Gson gson = new Gson();

    public static String getTransactionJson(Transaction t) {
        return gson.toJson(t, Transaction.class);
    }
}
