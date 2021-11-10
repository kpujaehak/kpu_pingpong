from flask import Flask
app = Flask(__name__)
@app.route('/')
def pong_service():
	return '[KPU_pong] Hello, I am pong container! nice to meet you!'
@app.route('/pong')
def do_pong():
	return '[KPU_pong] Hi kpu ping!'
if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5001, debug = True)
