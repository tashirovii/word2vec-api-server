import json
import urllib
import tornado.escape
from handlers.base import BaseHandler
from lib.vectorizer import Vectorizer

class SimilarHandler(BaseHandler):
    def get(self):
        words = self.get_argument("words")
        wordvector = Vectorizer(words)
        self.write(wordvector.load_similar())
