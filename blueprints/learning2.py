from flask import Blueprint


learning2_blueprint = Blueprint('learning2', __name__)

@learning2_blueprint.route('/<string:name>')
def home(name):
	return f"Hello by string parameter, \n{name}!"
	