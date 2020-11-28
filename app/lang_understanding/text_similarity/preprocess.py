import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from app.lang_understanding.text_similarity.stop_words_filtering import StopWords

nltk.download('punkt')

import string

class PreprocessText:
    def __init__(self):
        self.cleaned_tokens = None
        self.cleaned_text = None
        self.STOP_WORDS = StopWords().get_stop_words()

    def remove_spaces(self, text):
        text = text.strip()
        text = text.split()
        return ' '.join(text)

    def lower(self, text):
        return [i.lower() for i in text]

    def tokenize_sentence(self, abstracts):
        return [s for t in abstracts for s in sent_tokenize(t)]

    def tokenize_words(self, sentences):
        return word_tokenize(sentences)

    def remove_punctuation(self, tokens):
        first_filter = [word for word in tokens if word not in string.punctuation]
        # second_filter = [re.sub(r'[^\w\s]','',word) for word in first_filter if re.sub(r'[^\w\s]','',word)]
        return first_filter

    def remove_digits(self, tokens):
        first_filter = [word for word in tokens if word not in string.digits]
        # second_filter = [word for word in first_filter if not word.isdigit()]
        return first_filter

    def remove_stop_words(self, tokens):
        return [word for word in tokens if word not in self.STOP_WORDS]

    def get_cleaned_text_tokens(self):
        return self.cleaned_tokens

    def get_cleaned_text(self):
        return self.cleaned_text

    def clean(self, text):
       # tokenize_sentences_lst = self.tokenize_sentence(text)
        tokenized_words_lst = self.tokenize_words(text)
        tokenized_words_lst = self.lower(tokenized_words_lst)
        clean_tokens = self.remove_punctuation(tokenized_words_lst)
        clean_tokens = self.remove_digits(clean_tokens)
        clean_tokens = self.remove_stop_words(clean_tokens)
        self.cleaned_tokens = clean_tokens
        self.cleaned_text = [' '.join(x) for x in clean_tokens if x!=[]]