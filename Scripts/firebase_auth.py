import pyrebase

config = {
  "apiKey": "AIzaSyAZEcwvQqDuh1iTBrIZCDZUQqUALbYopds",
  "authDomain": "image-uploader-a579f.firebaseapp.com",
  "databaseURL": "https://image-uploader-a579f.firebaseio.com",
  "storageBucket": "image-uploader-a579f.appspot.com",
  
}

firebase = pyrebase.initialize_app(config)


