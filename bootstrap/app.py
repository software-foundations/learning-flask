from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template("/index.html")

@app.route('/index2', methods=['GET'])
def index2():
	return render_template("/index2.html")

@app.route('/index3', methods=['GET'])
def index3():
	return render_template("/index3.html")


if __name__ == '__main__':
	app.run('127.0.0.1', '5000', debug=True)
	