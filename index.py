'''
def app(environ, start_response):
	data = b"Hello, World!\n"
	start_response("200 OK", [
		("Content-Type", "text/plain"),
		("Content-Length", str(len(data)))
	])
	return iter([data])
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def source():
 html = 'Hello World!'
 return html
