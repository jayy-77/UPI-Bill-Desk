import urllib
import os
from firebase_admin import credentials, initialize_app, storage, firestore
import qrcode
import random

cred = credentials.Certificate('keys.json')
initialize_app(cred, {'storageBucket': 'upi-bill-desk.appspot.com'})
db = firestore.client()
db.collection("qr_data").document("reliance").set({'upi_url': None, 'amount': None})
def make_upi_qr(amount):
    payment_dict = {
        "pa": '8200639454398@paytm',
        "pn": 'jay prajapati',
        "tr": random.randint(10000, 99999),
        "tn": random.randint(1000, 9999),
        "am": amount,
        "cu": "INR"
    }
    upi_deep_link = "upi://pay" + '?' + urllib.parse.urlencode(payment_dict)
    img = qrcode.make(upi_deep_link)
    img.save('upi.png')
    store_qr_data(amount)
def store_qr_data(amount):
    bucket = storage.bucket()
    blob = bucket.blob('upi.png')
    blob.upload_from_filename('upi.png')
    db.collection("qr_data").document("reliance").update({'upi_url':blob.public_url,'amount':amount})
    os.remove('upi.png')
