import json

from flask import Blueprint
from .models import TalksType


module = Blueprint('talk', __name__, url_prefix='/talk')


@module.route('/talks_type/', methods=['GET'])
def talk_endpoint():
    talks_type_all = TalksType.query.all()
    result = []
    for talk_type_obj in talks_type_all:
        talk_type_dict = {}
        talk_type_dict["name"] = talk_type_obj.name
        talk_type_dict["img"] = talk_type_obj.image
        result.append(talk_type_dict)
    return json.dumps(result)