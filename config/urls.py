from handlers.ping import PingHandler
from handlers.wordvector import SimilarHandler

url_patterns = [
    ("/ping", PingHandler),
    ("/similar", SimilarHandler)
]
