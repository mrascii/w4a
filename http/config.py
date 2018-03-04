from pymongo import MongoClient
import uuid


WTF_CSRF_ENABLED = True
# SECRET_KEY = 'devil in the sky'
DB_NAME = 'w4a'

# DATABASE = MongoClient("mongodb://ant-login7.linux.crg.es:27017")[DB_NAME]
DATABASE = MongoClient()[DB_NAME]
INTROS = DATABASE.intros
INTROS_EN = DATABASE.intros_en
OBJECTS = DATABASE.objects
SPACES = DATABASE.chapters
SPACES_EN = DATABASE.chapters_en
CORE = DATABASE.core

MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=465
MAIL_USE_SSL=True
MAIL_USERNAME = 'wscibook@gmail.com'
MAIL_PASSWORD = 'pass4sci'
EMAILS = 'jescid@gmail.com, toni.amantonio@gmail.com'

# captcha
SECRET_KEY = str(uuid.uuid4())
CAPTCHA_ENABLE = True
CAPTCHA_NUMERIC_DIGITS = 7
SESSION_TYPE = 'mongodb'
SESSION_MONGODB_DB = 'w4a'

MONGOEXP = "/opt/mongodb/bin/mongoexport"
GEOCITY = "/home/jes/Code/w4a/geo/GeoLite2-City_20180206/GeoLite2-City.mmdb"

CSV = set(['csv', 'txt'])

DEBUG = True
PROPAGATE_EXCEPTIONS = True
