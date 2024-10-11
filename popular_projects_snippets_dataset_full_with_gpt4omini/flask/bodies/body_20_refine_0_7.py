from flask import Flask, request, session # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.app = Flask(__name__) # pragma: no cover
self.request = request # pragma: no cover
self.session = session # pragma: no cover

from flask import Flask, request, session # pragma: no cover
from werkzeug.middleware.proxy_fix import ProxyFix # pragma: no cover

class MockRequest: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.environ = {}  # Mocked WSGI environment # pragma: no cover
        self.session = session # pragma: no cover
        self.path = '/' # pragma: no cover
        self.method = 'GET' # pragma: no cover
        self.args = {} # pragma: no cover
        self.form = {} # pragma: no cover
 # pragma: no cover
class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.app = Flask(__name__) # pragma: no cover
self.app.wsgi_app = ProxyFix(self.app.wsgi_app) # pragma: no cover
self.request = MockRequest() # pragma: no cover
self.session = {'user_id': 123, 'username': 'test_user'} # pragma: no cover

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
