import json
import random

from flask import Blueprint
from .models import Retelling

module = Blueprint('summary', __name__, url_prefix='/summary')


@module.route('/random/', methods=['GET'])
def box_endpoint():
    retelling_all = Retelling.query.all()
    random_id = random.randint(0, len(retelling_all)-1)
    retelling = retelling_all[random_id]
    result = {"id": retelling.id, "title": retelling.title, "text": retelling.text}
    return json.dumps(result)