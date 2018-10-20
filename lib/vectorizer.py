import json
import gensim
from config.settings import MODEL_ROOT, MODEL_FILE

def load_vector_model():
    global model
    model = gensim.models.Word2Vec.load(MODEL_ROOT + MODEL_FILE)


class Vectorizer:
    def __init__(self, words):
        self.words = words.split(",")


    def load_similar(self):
        similars = {}
        for word in self.words:
            try:
                similar = model.most_similar(word)
                similars[word] = { key: value for (key, value) in similar }
            except KeyError:
                pass

        return json.dumps(similars, ensure_ascii=False)
