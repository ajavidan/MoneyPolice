package com.software.btc.moneypolice;

import android.os.AsyncTask;

import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

/**
 * Created by blair.javidan on 2/7/2017.
 */

public class HttpRequestTask extends AsyncTask<String, String, String> {


    @Override
    protected String doInBackground(String... params) {
        HttpURLConnection conn = null;

        try {
            URL url = new URL(params[0]);

            conn = (HttpURLConnection)url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Blair", "Awesome");
            conn.setDoOutput(true);
            conn.setDoInput(true);
            conn.setRequestProperty("User-Agent", "GYUserAgentAndroid");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.connect();
            String jsonParamsString = "{\"Armaghan\":\"Awesome\"}";

            DataOutputStream wr = new DataOutputStream (
                    conn.getOutputStream ());

            wr.writeBytes (jsonParamsString);
            wr.flush ();
            wr.close ();

            /*InputStream stream = conn.getInputStream();
            reader = new BufferedReader(new InputStreamReader(stream));

            StringBuffer buffer = new StringBuffer();

            String line = "";
            while ((line = reader.readLine()) != null){
                buffer.append(line);
            }
            return buffer.toString();*/

            //Get Response
            InputStream is = conn.getInputStream();
            BufferedReader rd = new BufferedReader(new InputStreamReader(is));
            String line;
            StringBuffer response = new StringBuffer();
            while((line = rd.readLine()) != null) {
                response.append(line);
                response.append('\r');
            }
            rd.close();
            return response.toString();

        } catch (Exception e) {

            e.printStackTrace();
            return null;

        } finally {

            if(conn != null) {
                conn.disconnect();
            }
        }
    }


}
