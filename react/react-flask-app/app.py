from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello', methods=['GET'])
def say_hello_world():
    return {'result': "Hello World"}

# if __name__ == '__main__':
# 	app.run("127.0.0.1", "5000", debug=True)
	