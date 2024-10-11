from flask import Flask # pragma: no cover
import typing as t # pragma: no cover

def create_app(script_info): return Flask(__name__) # pragma: no cover
set_debug_flag = True # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.create_app = None # pragma: no cover
        self.data = {} # pragma: no cover
        self.set_debug_flag = False # pragma: no cover
        self._loaded_app = None # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
#: Optionally the import path for the Flask application.
from l3.Runtime import _l_
self.app_import_path = app_import_path
_l_(16641)
#: Optionally a function that is passed the script info to create
#: the instance of the application.
self.create_app = create_app
_l_(16642)
#: A dictionary with arbitrary data that can be associated with
#: this script info.
self.data: t.Dict[t.Any, t.Any] = {}
_l_(16643)
self.set_debug_flag = set_debug_flag
_l_(16644)
self._loaded_app: Flask | None = None
_l_(16645)
