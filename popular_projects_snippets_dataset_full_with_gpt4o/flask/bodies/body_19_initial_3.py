import typing as t # pragma: no cover
from flask import Flask, Request, session # pragma: no cover
from werkzeug.exceptions import HTTPException # pragma: no cover
import contextvars # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
app = Flask(__name__) # pragma: no cover
request = None # pragma: no cover
environ = {} # pragma: no cover
Request = Request # pragma: no cover
HTTPException = HTTPException # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
self.app = app
_l_(22504)
if request is None:
    _l_(22507)

    request = app.request_class(environ)
    _l_(22505)
    request.json_module = app.json
    _l_(22506)
self.request: Request = request
_l_(22508)
self.url_adapter = None
_l_(22509)
try:
    _l_(22513)

    self.url_adapter = app.create_url_adapter(self.request)
    _l_(22510)
except HTTPException as e:
    _l_(22512)

    self.request.routing_exception = e
    _l_(22511)
self.flashes: t.Optional[t.List[t.Tuple[str, str]]] = None
_l_(22514)
self.session: t.Optional["SessionMixin"] = session
_l_(22515)
# Functions that should be executed after the request on the response
# object.  These will be called before the regular "after_request"
# functions.
self._after_request_functions: t.List[ft.AfterRequestCallable] = []
_l_(22516)

self._cv_tokens: t.List[t.Tuple[contextvars.Token, t.Optional[AppContext]]] = []
_l_(22517)
