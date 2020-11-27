from flask import Blueprint

module = Blueprint('talk', __name__, url_prefix='/talk')

@module.route('/', methods=['GET'])
def box_endpoint():
    return 'This talk!'