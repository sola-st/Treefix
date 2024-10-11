from flask import Flask, g # pragma: no cover
from typing import List # pragma: no cover
import contextvars # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
app = Flask(__name__) # pragma: no cover
app.app_ctx_globals_class = lambda: g # pragma: no cover
t = type('Mock', (object,), {'List': list}) # pragma: no cover
contextvars = type('Mock', (object,), {'Token': object}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
self.app = app
_l_(7548)
self.url_adapter = app.create_url_adapter(None)
_l_(7549)
self.g: _AppCtxGlobals = app.app_ctx_globals_class()
_l_(7550)
self._cv_tokens: t.List[contextvars.Token] = []
_l_(7551)
