import json
import  random

from flask import request
from flask import Blueprint

from .models import StartPhrases
from app.lang_understanding.chatbot.inference import get_answers


module = Blueprint('chat', __name__, url_prefix='/chat')


@module.route('/start_phrase/', methods=['GET'])
def box_endpoint():
    retelling_ids = StartPhrases.query.with_entities(StartPhrases.id).all()
    random_id = random.choice(retelling_ids)[0]
    retelling = StartPhrases.query.filter(StartPhrases.id == random_id).first()
    result = {"text": retelling.phrase}
    return json.dumps(result)

@module.route('/answer/', methods=['POST'])
def chat_answer():
    user_answer = json.loads(request.data)['text']

    model_answer = get_answers(user_answer)
    result = {"text": model_answer}
    return json.dumps(result)