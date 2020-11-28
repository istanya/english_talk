from scipy.spatial import distance
from app.lang_understanding.text_similarity.preprocess import PreprocessText
from app.lang_understanding.text_similarity.singeltonmodel import Singletonword2Vec
import numpy as np

def get_similarity(text1, text2):
    prep = PreprocessText()
    prep.clean(text1)
    tokens1 = prep.cleaned_tokens
    prep.clean(text2)
    tokens2 = prep.cleaned_tokens
    objw2v = Singletonword2Vec().w2vobj
    vector1 = np.zeros(300)
    vector2 = np.zeros(300)
    for i in tokens1:
        vector1 += objw2v.get_vector(i)
    for i in tokens2:
        vector2 += objw2v.get_vector(i)
    return distance.cosine(vector1, vector2)


text1 = 'hey cat'
text2 = 'hey brother'

score = get_similarity(text1, text2)
print(score)