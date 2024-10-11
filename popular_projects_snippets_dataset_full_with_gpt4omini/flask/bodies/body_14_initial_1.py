import contextvars # pragma: no cover
from typing import List # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
AppCtxGlobals = type('AppCtxGlobals', (object,), {})() # pragma: no cover
t = type('t', (), {'List': List}) # pragma: no cover
contextvars.Token = type('Token', (), {}) # pragma: no cover

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
