# 01 -> install python dependencies
pip install flask python-dotenv
pip install -U flask-cors

# 02 -> create app.py
touch app.py

# from flask import Flask
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route('/hello')
# def say_hello_world():
#     return {'result': "Hello World"}

# 03 -> create .env file
touch .env
# FLASK_APP=app.py
# FLASK_ENV=development

# 04 -> run server
flask run # python app.py works, too
