from flask import Flask
from learning import learning_blueprint
from learning2 import learning2_blueprint
from learning3 import learning3_blueprint

app = Flask(__name__)

app.register_blueprint(learning_blueprint)
app.register_blueprint(learning2_blueprint)
app.register_blueprint(learning3_blueprint, url_prefix='/greetings')

if __name__ == '__main__':
	app.run()
