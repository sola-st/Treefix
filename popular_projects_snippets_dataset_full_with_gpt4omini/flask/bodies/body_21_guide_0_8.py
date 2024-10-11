from werkzeug.exceptions import HTTPException # pragma: no cover
from flask import Request # pragma: no cover
from werkzeug.routing import Map, Rule # pragma: no cover

self = type('Mock', (object,), {'url_adapter': Map([Rule('/', endpoint='index')]), 'request': Request(environ={})})() # pragma: no cover
self.request.url_rule = None # pragma: no cover
self.request.view_args = {} # pragma: no cover
self.url_adapter.iter_rules = lambda: iter(self.url_adapter.rules) # pragma: no cover
self.url_adapter.match = lambda return_rule=False: (_ for _ in ()).throw(HTTPException('Not Found')) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
"""Can be overridden by a subclass to hook into the matching
        of the request.
        """
try:
    _l_(8169)

    result = self.url_adapter.match(return_rule=True)  # type: ignore
    _l_(8165)  # type: ignore
    self.request.url_rule, self.request.view_args = result  # type: ignore
    _l_(8166)  # type: ignore
except HTTPException as e:
    _l_(8168)

    self.request.routing_exception = e
    _l_(8167)
