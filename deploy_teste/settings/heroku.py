import environ 
from deploy_teste.settings.base import *

env = environ.Env()

DEBUG           = env.bool("DEBUG", False)

SECRET_KEY      = env("SECRETE_KEY")

ALLOWED_HOSTS   = env.list("ALLOWED_HOSTS")

DATABASES       = {
    "default": env.db(),
}