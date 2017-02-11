package com.software.btc.moneypolice;

import org.junit.Test;

/**
 * Created by blair.javidan on 2/11/2017.
 */

public class JsonUtiltest {


    @Test
    public void testJsonUtilTransaction() {

        Transaction t = new Transaction(new Fund("test", 0), 1);
        String testJson = t.toJsonString();
    }
}
