from flask import Flask
app = Flask(__name__)
import requests
@app.route('/')
def ping_service():
	return '[kpu_ping] Hello stranger, I am ping container! nice to meet u!!!!!!'
@app.route('/ping')
def do_ping():
		ping = '[kpu_ping] ---hello pong?-->'
		response = ' '
		try:
			response = requests.get('http://0.0.0.0:5051/pong')
		except requests.exceptions.RequestException as e:
			print('\n Cannot reach the pong service.\n')
			return 'ERROR\n'
		return '[kpu_ping] ---hello pong?-->' + response.text + ' \n'
if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5000, debug = True)
