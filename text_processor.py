import re
from os import listdir, stat

from nltk.stem.lancaster import LancasterStemmer
from json import JSONDecoder, JSONEncoder


# TODO: enter dir with the docs
class TextProcessor:
    def __init__(self):
        self.terms = []
        self.load_stopwords()

    def process(self, json):
        dec_json = JSONDecoder().decode(json)
        if dec_json['action'] == 'process':
            return self.lex_process(dec_json['data'])

    # load the stopwords (taken from nltk)
    def load_stopwords(self):
        self.stopwords = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
                              'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
                              'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
                              'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
                              'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
                              'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
                              'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
                              'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
                              'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
                              'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
                              'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
                              'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'])

    def lex_process(self, text):
        words = []
        for line in text.splitlines():
            for w in line.split():
                words.append(w.lower())
        return self.stemming(words)

    def remove_stopwords(self, words):
        return self.enc_json([w for w in words if w not in self.stopwords and w.isalpha()])

    def stemming(self, words):
        ps = LancasterStemmer()
        return self.remove_stopwords([ps.stem(w) for w in words])

    def enc_json(self, terms):
        output = JSONEncoder().encode({'terms': terms})
        return output
