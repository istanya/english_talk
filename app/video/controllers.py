import json
import random
from flask import request
from flask import Blueprint
from .models import Video
from app.lang_understanding.text_similarity.similarity import get_similarity

module = Blueprint('video', __name__, url_prefix='/video')


@module.route('/random/', methods=['GET'])
def video_endpoint():
    retelling_ids = Video.query.with_entities(Video.id).all()
    random_id = random.choice(retelling_ids)[0]
    retelling = Video.query.filter(Video.id == random_id).first()
    result = {"id": retelling.id, "title": retelling.title, "text": retelling.text}
    return json.dumps(result)


@module.route('<id>/result/', methods=['POST'])
def videoequal_endpoint(id):
    video = Video.query.with_entities(id).first()
    user_answer = request.form.get('user_answer')
    model_text = video.link
    similarity = get_similarity(user_answer, model_text)*100
    result = {"result": similarity}
    return json.dumps(result)