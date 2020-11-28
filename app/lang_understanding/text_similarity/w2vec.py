from gensim.models import KeyedVectors
from gensim.models import Word2Vec as Word2Vec_gensim
from os.path import join
import numpy as np


class Word2Vec():

    ''' Word2Vec model class '''
    def __init__(self, path_to_model=None, model_filename=None, embeddings_shape=None):
        self.path_to_model = path_to_model
        self.model_filename = model_filename
        self.embeddings_shape = embeddings_shape
        if path_to_model is None:
            raise AttributeError("path_to_model cannot be None")
        if model_filename is None:
            raise AttributeError("model_filename cannot be None")

    def load_model(self):
        self.loaded_model = Word2Vec_gensim.load(join(self.path_to_model, self.model_filename))

    def get_vector(self, word):
        try:
            return self.loaded_model[word]
        except:
            return np.ones(self.embeddings_shape)
