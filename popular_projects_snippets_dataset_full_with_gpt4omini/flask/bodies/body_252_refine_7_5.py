from flask import Flask # pragma: no cover
import typing as t # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
def create_app(): return Flask(__name__) # pragma: no cover
set_debug_flag = True # pragma: no cover

from flask import Flask # pragma: no cover
import typing as t # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
create_app = lambda: Flask(__name__) # pragma: no cover
self.create_app = create_app # pragma: no cover
self.data = {} # pragma: no cover
set_debug_flag = True # pragma: no cover
self.set_debug_flag = set_debug_flag # pragma: no cover
self._loaded_app = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
#: Optionally the import path for the Flask application.
from l3.Runtime import _l_
self.app_import_path = app_import_path
_l_(5005)
#: Optionally a function that is passed the script info to create
#: the instance of the application.
self.create_app = create_app
_l_(5006)
#: A dictionary with arbitrary data that can be associated with
#: this script info.
self.data: t.Dict[t.Any, t.Any] = {}
_l_(5007)
self.set_debug_flag = set_debug_flag
_l_(5008)
self._loaded_app: Flask | None = None
_l_(5009)
