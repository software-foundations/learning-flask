from flask import Blueprint


learning3_blueprint = Blueprint('learning3', __name__)

@learning3_blueprint.route('/<string:name>')
def home(name):
	return f"Hello string parameter by url_prefix, \n{name}!"
