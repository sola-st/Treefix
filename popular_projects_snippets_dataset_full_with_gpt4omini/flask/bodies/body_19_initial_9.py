from flask import Flask, Request, session # pragma: no cover
from werkzeug.exceptions import HTTPException # pragma: no cover
import typing as t # pragma: no cover
import contextvars # pragma: no cover
import functools as ft # pragma: no cover

self = type('MockSelf', (object,), {})() # pragma: no cover
app = Flask(__name__) # pragma: no cover
request = None # pragma: no cover
environ = {} # pragma: no cover
Request = Flask.request_class # pragma: no cover
HTTPException = HTTPException # pragma: no cover
SessionMixin = type('MockSessionMixin', (object,), {}) # pragma: no cover
session = SessionMixin() # pragma: no cover
contextvars = contextvars # pragma: no cover
AppContext = type('MockAppContext', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
self.app = app
_l_(4449)
if request is None:
    _l_(4452)

    request = app.request_class(environ)
    _l_(4450)
    request.json_module = app.json
    _l_(4451)
self.request: Request = request
_l_(4453)
self.url_adapter = None
_l_(4454)
try:
    _l_(4458)

    self.url_adapter = app.create_url_adapter(self.request)
    _l_(4455)
except HTTPException as e:
    _l_(4457)

    self.request.routing_exception = e
    _l_(4456)
self.flashes: t.Optional[t.List[t.Tuple[str, str]]] = None
_l_(4459)
self.session: t.Optional["SessionMixin"] = session
_l_(4460)
# Functions that should be executed after the request on the response
# object.  These will be called before the regular "after_request"
# functions.
self._after_request_functions: t.List[ft.AfterRequestCallable] = []
_l_(4461)

self._cv_tokens: t.List[t.Tuple[contextvars.Token, t.Optional[AppContext]]] = []
_l_(4462)
