from app import app
from flaskext.mysql import MySQL
import os

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE')
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('MYSQL_HOST')
mysql.init_app(app)