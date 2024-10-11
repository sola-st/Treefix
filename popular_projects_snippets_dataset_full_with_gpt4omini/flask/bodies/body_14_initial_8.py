from flask import Flask, g # pragma: no cover
import contextvars # pragma: no cover
import typing as t # pragma: no cover

app = Flask(__name__) # pragma: no cover
self = type('Mock', (object,), {'app': None, 'url_adapter': None, 'g': g, '_cv_tokens': []})() # pragma: no cover
self.app = app # pragma: no cover
self.url_adapter = app.create_url_adapter(None) # pragma: no cover
self._cv_tokens: t.List[contextvars.Token] = [] # pragma: no cover
app.create_url_adapter = lambda x: 'url_adapter_mock' # pragma: no cover
app.app_ctx_globals_class = lambda: 'app_ctx_globals_mock' # pragma: no cover
contextvars.Token = type('Token', (object,), {}) # pragma: no cover

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
