from flask import Flask
#import urlparse
from urllib.parse import urlparse
import psycopg2
import os

url = urlparse(os.environ['DATABASE_URL'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

con = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

app = Flask(__name__)

@app.route('/')
def source():
 html = 'В разработке!'
 return html
