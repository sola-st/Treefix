import os # pragma: no cover
from dotenv import load_dotenv, find_dotenv # pragma: no cover
from click import Context # pragma: no cover
from flask import Flask # pragma: no cover

get_load_dotenv = lambda x: True # pragma: no cover
class MockSelf: pass# pragma: no cover
self = MockSelf() # pragma: no cover
load_dotenv = lambda: None # pragma: no cover
extra = {} # pragma: no cover
class ScriptInfo:# pragma: no cover
    def __init__(self, create_app, set_debug_flag):# pragma: no cover
        self.create_app = create_app# pragma: no cover
        self.set_debug_flag = set_debug_flag# pragma: no cover
# pragma: no cover
extra['obj'] = ScriptInfo(create_app=lambda: Flask(__name__), set_debug_flag=lambda: None) # pragma: no cover
info_name = 'test_info' # pragma: no cover
args = [] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
# Set a flag to tell app.run to become a no-op. If app.run was
# not in a __name__ == __main__ guard, it would start the server
# when importing, blocking whatever command is being called.
from l3.Runtime import _l_
os.environ["FLASK_RUN_FROM_CLI"] = "true"
_l_(9315)

# Attempt to load .env and .flask env files. The --env-file
# option can cause another file to be loaded.
if get_load_dotenv(self.load_dotenv):
    _l_(9317)

    load_dotenv()
    _l_(9316)

if "obj" not in extra and "obj" not in self.context_settings:
    _l_(9319)

    extra["obj"] = ScriptInfo(
        create_app=self.create_app, set_debug_flag=self.set_debug_flag
    )
    _l_(9318)
aux = super().make_context(info_name, args, parent=parent, **extra)
_l_(9320)

exit(aux)
