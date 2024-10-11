from flask import Flask, session # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.secret_key = 'dummy_secret_key' # pragma: no cover
kwargs = {'environ_overrides': {}} # pragma: no cover
args = [] # pragma: no cover
outer_reqctx = None # pragma: no cover
_cv_request = type('MockCVRequest', (object,), {'get': lambda self, x: None, 'set': lambda self, x: 'token', 'reset': lambda self, x: None})() # pragma: no cover
app.session_interface = type('MockSessionInterface', (object,), {'open_session': lambda self, app, req: {}, 'is_null_session': lambda self, sess: False, 'save_session': lambda self, app, sess, resp: None})() # pragma: no cover

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
    _l_(4257)

    raise RuntimeError(
        "Session transactions only make sense with cookies enabled."
    )
    _l_(4256)
app = self.application
_l_(4258)
environ_overrides = kwargs.setdefault("environ_overrides", {})
_l_(4259)
self.cookie_jar.inject_wsgi(environ_overrides)
_l_(4260)
outer_reqctx = _cv_request.get(None)
_l_(4261)
with app.test_request_context(*args, **kwargs) as c:
    _l_(4276)

    session_interface = app.session_interface
    _l_(4262)
    sess = session_interface.open_session(app, c.request)
    _l_(4263)
    if sess is None:
        _l_(4265)

        raise RuntimeError(
            "Session backend did not open a session. Check the configuration"
        )
        _l_(4264)

    # Since we have to open a new request context for the session
    # handling we want to make sure that we hide out own context
    # from the caller.  By pushing the original request context
    # (or None) on top of this and popping it we get exactly that
    # behavior.  It's important to not use the push and pop
    # methods of the actual request context object since that would
    # mean that cleanup handlers are called
    token = _cv_request.set(outer_reqctx)  # type: ignore[arg-type]
    _l_(4266)  # type: ignore[arg-type]
    try:
        _l_(4270)

        aux = sess
        _l_(4267)
        exit(aux)
    finally:
        _l_(4269)

        _cv_request.reset(token)
        _l_(4268)

    resp = app.response_class()
    _l_(4271)
    if not session_interface.is_null_session(sess):
        _l_(4273)

        session_interface.save_session(app, sess, resp)
        _l_(4272)
    headers = resp.get_wsgi_headers(c.request.environ)
    _l_(4274)
    self.cookie_jar.extract_wsgi(c.request.environ, headers)
    _l_(4275)
