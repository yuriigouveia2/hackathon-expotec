WTF_CSRF_ENABLED = True
SECRET_KEY = "you-will-never-guess"

import os
basedir = os.path.abspath(os.path.dirname(__file__))

MONGO_URI = 'mongodb://localhost:27017/restdb'
MONGO_DBNAME = 'restdb'