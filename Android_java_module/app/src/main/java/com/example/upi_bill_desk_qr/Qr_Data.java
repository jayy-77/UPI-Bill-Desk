package com.example.upi_bill_desk_qr;

public class Qr_Data {
    String qr_uri;
    int amount;

    public Qr_Data(){

    }
    public Qr_Data(String qr_uri, int amount){
        this.qr_uri = qr_uri;
        this.amount = amount;
    }
    public String getQr_uri() {
        return qr_uri;
    }

    public void setQr_uri(String qr_uri) {
        this.qr_uri = qr_uri;
    }

    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
}

