import os
class Config(object):
   SECRET_KY = os.environment.get('SECRET_KEY') or "secret_string"
