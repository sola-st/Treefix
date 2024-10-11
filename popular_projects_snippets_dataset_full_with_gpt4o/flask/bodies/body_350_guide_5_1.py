from flask import Flask, request, session # pragma: no cover
from flask.sessions import SecureCookieSessionInterface # pragma: no cover
from contextvars import ContextVar # pragma: no cover

class MockCookieJar: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.cookies_enabled = False # pragma: no cover
    def inject_wsgi(self, environ_overrides): # pragma: no cover
        pass # pragma: no cover
    def extract_wsgi(self, environ, headers): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MockSessionInterface(SecureCookieSessionInterface): # pragma: no cover
    def open_session(self, app, request): # pragma: no cover
        return {'key': 'value'}  # Non-null session # pragma: no cover
    def save_session(self, app, session, response): # pragma: no cover
        pass # pragma: no cover
    def is_null_session(self, sess): # pragma: no cover
        return False # pragma: no cover
 # pragma: no cover
app = Flask(__name__) # pragma: no cover
app.secret_key = 'supersecretkey' # pragma: no cover
app.session_interface = MockSessionInterface() # pragma: no cover
_cv_request = ContextVar('request_context') # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), {'application': app, 'cookie_jar': MockCookieJar()})() # pragma: no cover
args = [] # pragma: no cover
kwargs = {} # pragma: no cover
 # pragma: no cover
# Manually disable cookies to trigger RuntimeError # pragma: no cover
self.cookie_jar.cookies_enabled = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/testing.py
from l3.Runtime import _l_
"""When used in combination with a ``with`` statement this opens a
        session transaction.  This can be used to modify the session that
        the test client uses.  Once the ``with`` block is left the session is
        stored back.

        ::

            with client.session_transaction() as session:
                session['value'] = 42

        Internally this is implemented by going through a temporary test
        request context and since session handling could depend on
        request variables this function accepts the same arguments as
        :meth:`~flask.Flask.test_request_context` which are directly
        passed through.
        """
if self.cookie_jar is None:
    _l_(15874)

    raise RuntimeError(
        "Session transactions only make sense with cookies enabled."
    )
    _l_(15873)
app = self.application
_l_(15875)
environ_overrides = kwargs.setdefault("environ_overrides", {})
_l_(15876)
self.cookie_jar.inject_wsgi(environ_overrides)
_l_(15877)
outer_reqctx = _cv_request.get(None)
_l_(15878)
with app.test_request_context(*args, **kwargs) as c:
    _l_(15893)

    session_interface = app.session_interface
    _l_(15879)
    sess = session_interface.open_session(app, c.request)
    _l_(15880)
    if sess is None:
        _l_(15882)

        raise RuntimeError(
            "Session backend did not open a session. Check the configuration"
        )
        _l_(15881)

    # Since we have to open a new request context for the session
    # handling we want to make sure that we hide out own context
    # from the caller.  By pushing the original request context
    # (or None) on top of this and popping it we get exactly that
    # behavior.  It's important to not use the push and pop
    # methods of the actual request context object since that would
    # mean that cleanup handlers are called
    token = _cv_request.set(outer_reqctx)  # type: ignore[arg-type]
    _l_(15883)  # type: ignore[arg-type]
    try:
        _l_(15887)

        aux = sess
        _l_(15884)
        exit(aux)
    finally:
        _l_(15886)

        _cv_request.reset(token)
        _l_(15885)

    resp = app.response_class()
    _l_(15888)
    if not session_interface.is_null_session(sess):
        _l_(15890)

        session_interface.save_session(app, sess, resp)
        _l_(15889)
    headers = resp.get_wsgi_headers(c.request.environ)
    _l_(15891)
    self.cookie_jar.extract_wsgi(c.request.environ, headers)
    _l_(15892)
