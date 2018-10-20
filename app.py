import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

from config.settings import settings
from config.urls import url_patterns
from lib.vectorizer import load_vector_model

class Word2VecApi(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    app = Word2VecApi()
    load_vector_model()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
