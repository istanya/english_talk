from app.lang_understanding.text_similarity.w2vec import Word2Vec

class Singletonword2Vec(object):
    exist = False

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singletonword2Vec, cls).__new__(cls)
        else:
            cls.exist = True
        return cls.instance

    def __init__(self):
        if not self.exist:
            self.w2vobj = Word2Vec(path_to_model='data/Word2vec/', model_filename='base_model.model', embeddings_shape=300)
            self.w2vobj.load_model()




