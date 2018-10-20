import json
import tornado.web

import logging
logger = logging.getLogger(__name__)

class BaseHandler(tornado.web.RequestHandler):
    def load_json(self):
        try:
            self.request.arguments = json.loads(self.request.body)
        except ValueError:
            msg = "Could not decode JSON: %s" % self.request.body
            logger.debug(msg)
            raise tornado.web.HTTPError(400, msg)
