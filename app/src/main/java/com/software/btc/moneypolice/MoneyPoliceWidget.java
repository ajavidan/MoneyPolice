package com.software.btc.moneypolice;

import android.app.PendingIntent;
import android.appwidget.AppWidgetManager;
import android.appwidget.AppWidgetProvider;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.widget.RemoteViews;

/**
 * Implementation of App Widget functionality.
 */
public class MoneyPoliceWidget extends AppWidgetProvider {

    public static int amount = 0;
     void updateAppWidget(Context context, AppWidgetManager appWidgetManager,
                                int appWidgetId) {

        CharSequence widgetText = context.getString(R.string.appwidget_text);
        // Construct the RemoteViews object
        RemoteViews views = new RemoteViews(context.getPackageName(), R.layout.money_police_widget);
         views.setTextViewText(R.id.appwidget_text, widgetText);

         views.setOnClickPendingIntent(R.id.food_button, getSelfIntent(context, "SendFood"));
         views.setOnClickPendingIntent(R.id.grocery_button, getSelfIntent(context, "SendGrocery"));
         views.setOnClickPendingIntent(R.id.candy_button, getSelfIntent(context, "SendCandy"));
         views.setOnClickPendingIntent(R.id.fun_button, getSelfIntent(context, "SendFun"));
         views.setOnClickPendingIntent(R.id.other_button, getSelfIntent(context, "SendOther"));
         views.setOnClickPendingIntent(R.id.bill_button, getSelfIntent(context, "SendBill"));
         views.setOnClickPendingIntent(R.id.button_clear, getSelfIntent(context, "Clear"));
         views.setOnClickPendingIntent(R.id.button_1, getSelfIntent(context, "Add_1"));
         views.setOnClickPendingIntent(R.id.button_5, getSelfIntent(context, "Add_5"));
         views.setOnClickPendingIntent(R.id.button_10, getSelfIntent(context, "Add_10"));
         views.setOnClickPendingIntent(R.id.button_20, getSelfIntent(context, "Add_20"));
         views.setOnClickPendingIntent(R.id.button_50, getSelfIntent(context, "Add_50"));
         views.setOnClickPendingIntent(R.id.button_100, getSelfIntent(context, "Add_100"));

         // Instruct the widget manager to update the widget
        appWidgetManager.updateAppWidget(appWidgetId, views);
    }

    protected PendingIntent getSelfIntent(Context context, String action){
        Intent intent = new Intent(context, getClass());
        intent.setAction(action);
        return PendingIntent.getBroadcast(context, 0, intent, 0);
    }

    @Override
    public void onReceive(Context context, Intent intent){
        super.onReceive(context, intent);

        String action = intent.getAction();
        if(action.substring(0,4).equals("Send")){
            sendFundAmount(context, action.substring(4));
            return;
        }
        if(action.substring(0,4).equals("Add")) {
            addAmount(context, Integer.parseInt(action.substring(4)));
            return;
        }
    }

    private void sendFundAmount(Context context, String fundName){
        AppWidgetManager manager = AppWidgetManager.getInstance(context);
        RemoteViews views = new RemoteViews(context.getPackageName(), R.layout.money_police_widget);
        Transaction transaction = new Transaction(new Fund(fundName, amount), 1);
        TransactionDealer transactionDealer = new TransactionDealer(views, transaction);
        transactionDealer.sendTransaction("https://httpbin.org/post");
        // Reset amount to 0
        amount = 0;
        views.setTextViewText(R.id.amount, "0.00");
        views.setInt(R.id.food_button, "setBackgroundColor", Color.parseColor("#1aaf00"));
        manager.updateAppWidget(new ComponentName(context, MoneyPoliceWidget.class), views);
    }

    private void addAmount(Context context, int addAmount){
        amount += addAmount;
        AppWidgetManager manager = AppWidgetManager.getInstance(context);
        RemoteViews views = new RemoteViews(context.getPackageName(), R.layout.money_police_widget);
        views.setTextViewText(R.id.amount, amount + ".00");
        manager.updateAppWidget(new ComponentName(context, MoneyPoliceWidget.class), views);
    }

    private void clear(Context context){
        amount = 0;
        AppWidgetManager manager = AppWidgetManager.getInstance(context);
        RemoteViews views = new RemoteViews(context.getPackageName(), R.layout.money_police_widget);
        views.setTextViewText(R.id.amount, "0.00");
        manager.updateAppWidget(new ComponentName(context, MoneyPoliceWidget.class), views);
    }

    @Override
    public void onUpdate(Context context, AppWidgetManager appWidgetManager, int[] appWidgetIds) {
        // There may be multiple widgets active, so update all of them
        for (int appWidgetId : appWidgetIds) {
            updateAppWidget(context, appWidgetManager, appWidgetId);
        }
    }

    @Override
    public void onEnabled(Context context) {
        // Enter relevant functionality for when the first widget is created
    }

    @Override
    public void onDisabled(Context context) {
        // Enter relevant functionality for when the last widget is disabled
    }

}

