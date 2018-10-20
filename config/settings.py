import sys
import os
import tornado
from tornado.options import define, options
from base64 import b64encode
from uuid import uuid4

path = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(sys.modules['__main__'].__file__)
MEDIA_ROOT = path(ROOT, "media")
MODEL_ROOT = path(MEDIA_ROOT, "models")
MODEL_FILE = "/ja.bin"

# tornadoの設定
define("port", default=8888, help="tornado port", type=int)
define("config", default=None, help="tornado config")
tornado.options.parse_command_line()

settings = {}
settings["static_path"] = MEDIA_ROOT
settings["cookie_secret"] = b64encode(uuid4().bytes + uuid4().bytes)
