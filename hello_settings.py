import os, json


# project path
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
print 'PROJECT_PATH: {}'.format(PROJECT_PATH)


# secrets dict
SECRETS_PATH = os.path.join(PROJECT_PATH, 'secret.json')
SECRETS_DICT = json.loads(open(SECRETS_PATH, "r").read())


# are we local?
LOCAL = os.environ.get('LOCAL')
DEBUG = LOCAL


# temporary settings below
