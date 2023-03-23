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
    security_code = random.randint(1000, 9999)
    payment_dict = {
        "pa": '8200639454398@paytm',
        "pn": 'jay prajapati',
        "tr": random.randint(10000, 99999),
        "tn": security_code,
        "am": amount,
        "cu": "INR"
    }
    upi_deep_link = "upi://pay" + '?' + urllib.parse.urlencode(payment_dict)
    img = qrcode.make(upi_deep_link)
    img_name = "qr.png"
    img.save(img_name)
    print("Security Code: ",security_code)
    store_qr_data(amount,img_name)
def store_qr_data(amount,img_name):
    bucket = storage.bucket()
    blob = bucket.blob(img_name)
    blob.upload_from_filename(img_name)
    blob.make_public()
    db.collection("qr_data").document("reliance").update({'upi_url':str(blob.public_url),'amount':amount})
    os.remove(img_name)