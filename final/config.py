import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'secret'
MAX_SEARCH_RESULTS = 50
OPENID_PROVIDERS = [

    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' }
]
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<flask>:<lxk568568>@<flasktest.cvnpw8ld1fvy.us-east-1.rds.amazonaws.com:3306>/<app>'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WHOOSH_BASE = os.path.join(basedir, 'search.db')
WHOOSH_ENABLED = os.environ.get('HEROKU') is None
MAX_SEARCH_RESULTS = 50

