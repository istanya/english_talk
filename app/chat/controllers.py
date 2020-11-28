import json
import  random

from flask import Blueprint
from .models import StartPhrases


module = Blueprint('chat', __name__, url_prefix='/chat')


@module.route('/start_phrase/', methods=['GET'])
def box_endpoint():
    retelling_ids = StartPhrases.query.with_entities(StartPhrases.id).all()
    random_id = random.choice(retelling_ids)[0]
    retelling = StartPhrases.query.filter(StartPhrases.id == random_id).first()
    result = {"text": retelling.phrase}
    return json.dumps(result)