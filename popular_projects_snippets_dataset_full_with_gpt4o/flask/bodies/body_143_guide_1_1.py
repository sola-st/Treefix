from flask import Flask, Blueprint, request # pragma: no cover
from flask.ctx import _cv_app, _cv_request # pragma: no cover
from werkzeug.routing import BuildError # pragma: no cover

class MockUrlAdapter: # pragma: no cover
    def build(self, endpoint, values, method=None, url_scheme=None, force_external=None): # pragma: no cover
        return f'/mocked_url_for/{endpoint}' # pragma: no cover
 # pragma: no cover
class MockRequest: # pragma: no cover
    def __init__(self, blueprint): # pragma: no cover
        self.blueprint = blueprint # pragma: no cover
 # pragma: no cover
class MockRequestContext: # pragma: no cover
    def __init__(self, blueprint): # pragma: no cover
        self.url_adapter = MockUrlAdapter() # pragma: no cover
        self.request = MockRequest(blueprint) # pragma: no cover
 # pragma: no cover
cv_request = MockRequestContext(None) # pragma: no cover
_cv_app.set(None) # pragma: no cover
_cv_request.set(cv_request) # pragma: no cover
 # pragma: no cover
class MockAppContext: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.url_adapter = MockUrlAdapter() # pragma: no cover
 # pragma: no cover
_cv_app.set(MockAppContext()) # pragma: no cover
_cv_request.set(None) # pragma: no cover
 # pragma: no cover
class MockApp: # pragma: no cover
    def create_url_adapter(self, x): # pragma: no cover
        return None # pragma: no cover
    def inject_url_defaults(self, endpoint, values): # pragma: no cover
        pass # pragma: no cover
    def handle_url_build_error(self, error, endpoint, values): # pragma: no cover
        return 'handle_error' # pragma: no cover
 # pragma: no cover
self = MockApp() # pragma: no cover
 # pragma: no cover
sys.modules['_cv_app'] = _cv_app # pragma: no cover
sys.modules['_cv_request'] = _cv_request # pragma: no cover
sys.modules['request'] = request # pragma: no cover
 # pragma: no cover
endpoint = 'invalid_endpoint' # pragma: no cover
values = {} # pragma: no cover
_anchor = None # pragma: no cover
_method = None # pragma: no cover
_scheme = None # pragma: no cover
_external = None # pragma: no cover
aux = None # pragma: no cover
def url_quote(anchor): # pragma: no cover
    return anchor # pragma: no cover
exit = print # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Generate a URL to the given endpoint with the given values.

        This is called by :func:`flask.url_for`, and can be called
        directly as well.

        An *endpoint* is the name of a URL rule, usually added with
        :meth:`@app.route() <route>`, and usually the same name as the
        view function. A route defined in a :class:`~flask.Blueprint`
        will prepend the blueprint's name separated by a ``.`` to the
        endpoint.

        In some cases, such as email messages, you want URLs to include
        the scheme and domain, like ``https://example.com/hello``. When
        not in an active request, URLs will be external by default, but
        this requires setting :data:`SERVER_NAME` so Flask knows what
        domain to use. :data:`APPLICATION_ROOT` and
        :data:`PREFERRED_URL_SCHEME` should also be configured as
        needed. This config is only used when not in an active request.

        Functions can be decorated with :meth:`url_defaults` to modify
        keyword arguments before the URL is built.

        If building fails for some reason, such as an unknown endpoint
        or incorrect values, the app's :meth:`handle_url_build_error`
        method is called. If that returns a string, that is returned,
        otherwise a :exc:`~werkzeug.routing.BuildError` is raised.

        :param endpoint: The endpoint name associated with the URL to
            generate. If this starts with a ``.``, the current blueprint
            name (if any) will be used.
        :param _anchor: If given, append this as ``#anchor`` to the URL.
        :param _method: If given, generate the URL associated with this
            method for the endpoint.
        :param _scheme: If given, the URL will have this scheme if it
            is external.
        :param _external: If given, prefer the URL to be internal
            (False) or require it to be external (True). External URLs
            include the scheme and domain. When not in an active
            request, URLs are external by default.
        :param values: Values to use for the variable parts of the URL
            rule. Unknown keys are appended as query string arguments,
            like ``?a=b&c=d``.

        .. versionadded:: 2.2
            Moved from ``flask.url_for``, which calls this method.
        """
req_ctx = _cv_request.get(None)
_l_(20168)

if req_ctx is not None:
    _l_(20185)

    url_adapter = req_ctx.url_adapter
    _l_(20169)
    blueprint_name = req_ctx.request.blueprint
    _l_(20170)

    # If the endpoint starts with "." and the request matches a
    # blueprint, the endpoint is relative to the blueprint.
    if endpoint[:1] == ".":
        _l_(20174)

        if blueprint_name is not None:
            _l_(20173)

            endpoint = f"{blueprint_name}{endpoint}"
            _l_(20171)
        else:
            endpoint = endpoint[1:]
            _l_(20172)

            # When in a request, generate a URL without scheme and
            # domain by default, unless a scheme is given.
    if _external is None:
        _l_(20176)

        _external = _scheme is not None
        _l_(20175)
else:
    app_ctx = _cv_app.get(None)
    _l_(20177)

    # If called by helpers.url_for, an app context is active,
    # use its url_adapter. Otherwise, app.url_for was called
    # directly, build an adapter.
    if app_ctx is not None:
        _l_(20180)

        url_adapter = app_ctx.url_adapter
        _l_(20178)
    else:
        url_adapter = self.create_url_adapter(None)
        _l_(20179)

    if url_adapter is None:
        _l_(20182)

        raise RuntimeError(
            "Unable to build URLs outside an active request"
            " without 'SERVER_NAME' configured. Also configure"
            " 'APPLICATION_ROOT' and 'PREFERRED_URL_SCHEME' as"
            " needed."
        )
        _l_(20181)

    # When outside a request, generate a URL with scheme and
    # domain by default.
    if _external is None:
        _l_(20184)

        _external = True
        _l_(20183)
if _scheme is not None and not _external:
    _l_(20187)

    raise ValueError("When specifying '_scheme', '_external' must be True.")
    _l_(20186)

self.inject_url_defaults(endpoint, values)
_l_(20188)

try:
    _l_(20193)

    rv = url_adapter.build(  # type: ignore[union-attr]
        endpoint,
        values,
        method=_method,
        url_scheme=_scheme,
        force_external=_external,
    )
    _l_(20189)
except BuildError as error:
    _l_(20192)

    values.update(
        _anchor=_anchor, _method=_method, _scheme=_scheme, _external=_external
    )
    _l_(20190)
    aux = self.handle_url_build_error(error, endpoint, values)
    _l_(20191)
    exit(aux)

if _anchor is not None:
    _l_(20195)

    rv = f"{rv}#{url_quote(_anchor)}"
    _l_(20194)
aux = rv
_l_(20196)

exit(aux)
