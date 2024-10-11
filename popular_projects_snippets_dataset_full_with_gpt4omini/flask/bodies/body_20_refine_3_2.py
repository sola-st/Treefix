from flask import Flask, Request, session # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.app = Flask(__name__) # pragma: no cover
self.request = Request(environ={'REQUEST_METHOD': 'GET', 'PATH_INFO': '/'}) # pragma: no cover
self.session = {} # pragma: no cover

from flask import Flask, Request, session # pragma: no cover

class MockApp: pass # pragma: no cover
class MockRequest(Request): pass # pragma: no cover
class MockSession: pass # pragma: no cover
self = type('Mock', (object,), {'app': MockApp(), 'request': MockRequest(environ={'REQUEST_METHOD': 'GET', 'PATH_INFO': '/'}), 'session': MockSession()})() # pragma: no cover
self.__class__ = type('MockClass', (object,), {'__init__': lambda self, app, environ, request, session: None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
"""Creates a copy of this request context with the same request object.
        This can be used to move a request context to a different greenlet.
        Because the actual request object is the same this cannot be used to
        move a request context to a different thread unless access to the
        request object is locked.

        .. versionadded:: 0.10

        .. versionchanged:: 1.1
           The current session object is used instead of reloading the original
           data. This prevents `flask.session` pointing to an out-of-date object.
        """
aux = self.__class__(
    self.app,
    environ=self.request.environ,
    request=self.request,
    session=self.session,
)
_l_(6895)
exit(aux)
