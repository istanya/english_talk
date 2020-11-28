from nltk.corpus import stopwords as stopwords_nltk
import nltk
nltk.download('stopwords')

class StopWords:
    def __init__(self):
        ...

    def get_stop_words(self):
        nltk_stop_words = stopwords_nltk.words('english')
        return nltk_stop_words