import json
import random

from flask import Blueprint
from .models import Retelling

module = Blueprint('summary', __name__, url_prefix='/summary')


@module.route('/random/', methods=['GET'])
def box_endpoint():
    retelling_ids = Retelling.query.with_entities(Retelling.id).all()
    random_id = random.choice(retelling_ids)[0]
    retelling = Retelling.query.filter(Retelling.id == random_id).first()
    result = {"id": retelling.id, "title": retelling.title, "text": retelling.text}
    return json.dumps(result)