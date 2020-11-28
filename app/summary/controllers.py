import json
import random
from flask import request
from flask import Blueprint
from .models import Retelling
from app.lang_understanding.text_similarity.similarity import get_similarity

module = Blueprint('summary', __name__, url_prefix='/summary')


@module.route('/random/', methods=['GET'])
def summary_endpoint():
    retelling_ids = Retelling.query.with_entities(Retelling.id).all()
    random_id = random.choice(retelling_ids)[0]
    retelling = Retelling.query.filter(Retelling.id == random_id).first()
    result = {"id": retelling.id, "title": retelling.title, "text": retelling.text}
    return json.dumps(result)


@module.route('/summary/<id>/result/', methods=['POST'])
def summaryequal_endpoint(id):
    retelling = Retelling.query.with_entities(id).first()
    user_answer = request.form.get('user_text')
    model_text = retelling.summary
    similarity = get_similarity(user_answer, model_text)*100
    result = {"result": similarity}
    return json.dumps(result)