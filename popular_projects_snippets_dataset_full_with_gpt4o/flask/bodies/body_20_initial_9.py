from flask import Flask, Request, session # pragma: no cover
import os # pragma: no cover

self = type('Mock', (object,), {'__class__': lambda self: self.__class__, 'app': None, 'request': None, 'session': None})() # pragma: no cover
self.app = Flask(__name__) # pragma: no cover
self.request = Request({'wsgi.url_scheme': 'http', 'SERVER_NAME': 'localhost', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/', 'SERVER_PORT': '5000', 'wsgi.version': (1, 0), 'wsgi.input': os.fdopen(os.dup(0), 'rb'), 'wsgi.errors': os.fdopen(os.dup(2), 'wb') }) # pragma: no cover
self.session = session # pragma: no cover

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
_l_(18192)
exit(aux)
