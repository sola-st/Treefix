from typing import Optional, List, Tuple, Callable # pragma: no cover
from werkzeug.exceptions import HTTPException # pragma: no cover
from werkzeug.datastructures import ImmutableMultiDict # pragma: no cover
from werkzeug.wrappers import Request # pragma: no cover
import contextvars # pragma: no cover
from flask import session # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
app = type('Mock', (object,), {'request_class': Request, 'json': None, 'create_url_adapter': lambda req: 'url_adapter'})() # pragma: no cover
request = None # pragma: no cover
environ = {} # pragma: no cover
Request = type('Mock', (object,), {}) # pragma: no cover
HTTPException = type('Mock', (Exception,), {}) # pragma: no cover
t = type('Mock', (object,), {'Optional': Optional, 'List': List, 'Tuple': Tuple}) # pragma: no cover
session = type('Mock', (object,), {}) # pragma: no cover
ft = type('Mock', (object,), {'AfterRequestCallable': Callable}) # pragma: no cover
contextvars = type('Mock', (object,), {'Token': object}) # pragma: no cover
AppContext = type('Mock', (object,), {}) # pragma: no cover

from typing import Optional, List, Tuple, Callable # pragma: no cover
from werkzeug.exceptions import HTTPException # pragma: no cover
from werkzeug.wrappers import Request # pragma: no cover
import contextvars # pragma: no cover
from flask import session # pragma: no cover

self = type('Mock', (object,), {'flashes': None, 'session': None, '_after_request_functions': [], '_cv_tokens': []})() # pragma: no cover
app = type('Mock', (object,), {'request_class': Request, 'json': None, 'create_url_adapter': lambda self, req: 'url_adapter'})() # pragma: no cover
environ = {} # pragma: no cover
Request = type('Mock', (object,), {}) # pragma: no cover
HTTPException = type('Mock', (Exception,), {}) # pragma: no cover
t = type('Mock', (object,), {'Optional': Optional, 'List': List, 'Tuple': Tuple}) # pragma: no cover
session = type('Mock', (object,), {}) # pragma: no cover
ft = type('Mock', (object,), {'AfterRequestCallable': Callable}) # pragma: no cover
contextvars = type('Mock', (object,), {'Token': object}) # pragma: no cover
AppContext = type('Mock', (object,), {}) # pragma: no cover

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
