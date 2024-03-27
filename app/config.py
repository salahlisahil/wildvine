import os
from datetime import timedelta
from pathlib import Path
import redis

SECRET_KEY = os.urandom(16)
path = Path(__file__).parent.absolute()
SQLALCHEMY_DATABASE_URI = f'sqlite:///{path}/db/flask.db'

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

redis_store = redis.StrictRedis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

SESSION_TYPE = 'redis'
SESSION_REDIS = redis_store
# SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
REMEMBER_COOKIE_DURATION = 3600
SESSION_PERMANENT = True
PERMANENT_SESSION_LIFETIME = timedelta(days=7)

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_USE_TLS = True
MAIL_USE_SSL = False
