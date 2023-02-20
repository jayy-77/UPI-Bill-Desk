from firebase_admin import credentials, initialize_app, storage

cred = credentials.Certificate('keys.json')
initialize_app(cred, {'storageBucket': 'upi-bill-desk.appspot.com'})

bucket = storage.bucket()
blob = bucket.blob('qr.jpg')
blob.upload_from_filename('qr.jpg')
print("your file url", blob.public_url)
