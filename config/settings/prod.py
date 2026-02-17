from .base import *
from decouple import config

DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")])

STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"

if os.getenv("CI") == "true":
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_BROKER_DB = 0
    REDIS_RESULT_DB = 0
else:
    REDIS_HOST = config("REDIS_HOST", default="redis")
    REDIS_PORT = config("REDIS_PORT", default=6379, cast=int)
    REDIS_BROKER_DB = config("REDIS_BROKER_DB", default=0, cast=int)
    REDIS_RESULT_DB = config("REDIS_RESULT_DB", default=0, cast=int)

CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_BROKER_DB}"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_RESULT_DB}"
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
