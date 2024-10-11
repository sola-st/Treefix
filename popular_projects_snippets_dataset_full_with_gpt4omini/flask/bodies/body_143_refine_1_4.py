from flask import Flask, request, Blueprint # pragma: no cover
from werkzeug.routing import BuildError # pragma: no cover
from urllib.parse import quote as url_quote # pragma: no cover

endpoint = 'example_endpoint' # pragma: no cover
_external = None # pragma: no cover
_scheme = 'https' # pragma: no cover
_cv_app = Flask(__name__).app_context() # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
values = {'param1': 'value1', 'param2': 'value2'} # pragma: no cover
_method = 'GET' # pragma: no cover
_anchor = 'section1' # pragma: no cover

from flask import Flask, request, Blueprint, url_for # pragma: no cover
from werkzeug.routing import BuildError # pragma: no cover
from werkzeug.routing import Map, Rule # pragma: no cover
from urllib.parse import quote as url_quote # pragma: no cover

_cv_request = type('MockRequestContext', (object,), {'url_adapter': None, 'request': request})() # pragma: no cover
endpoint = 'example_endpoint' # pragma: no cover
_external = None # pragma: no cover
_scheme = 'https' # pragma: no cover
_cv_app = Flask(__name__).app_context() # pragma: no cover
class MockURLAdapter: # pragma: no cover
    def build(self, endpoint, values, method=None, url_scheme=None, force_external=None): # pragma: no cover
        return f'http://example.com/{endpoint}' # pragma: no cover
self = type('Mock', (object,), {'create_url_adapter': lambda self, arg: MockURLAdapter(), 'inject_url_defaults': lambda self, endpoint, values: None, 'handle_url_build_error': lambda self, error, endpoint, values: 'error_handling_response'})() # pragma: no cover
values = {'param1': 'value1', 'param2': 'value2'} # pragma: no cover
_method = 'GET' # pragma: no cover
_anchor = 'section1' # pragma: no cover

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
_l_(9109)

if req_ctx is not None:
    _l_(9126)

    url_adapter = req_ctx.url_adapter
    _l_(9110)
    blueprint_name = req_ctx.request.blueprint
    _l_(9111)

    # If the endpoint starts with "." and the request matches a
    # blueprint, the endpoint is relative to the blueprint.
    if endpoint[:1] == ".":
        _l_(9115)

        if blueprint_name is not None:
            _l_(9114)

            endpoint = f"{blueprint_name}{endpoint}"
            _l_(9112)
        else:
            endpoint = endpoint[1:]
            _l_(9113)

            # When in a request, generate a URL without scheme and
            # domain by default, unless a scheme is given.
    if _external is None:
        _l_(9117)

        _external = _scheme is not None
        _l_(9116)
else:
    app_ctx = _cv_app.get(None)
    _l_(9118)

    # If called by helpers.url_for, an app context is active,
    # use its url_adapter. Otherwise, app.url_for was called
    # directly, build an adapter.
    if app_ctx is not None:
        _l_(9121)

        url_adapter = app_ctx.url_adapter
        _l_(9119)
    else:
        url_adapter = self.create_url_adapter(None)
        _l_(9120)

    if url_adapter is None:
        _l_(9123)

        raise RuntimeError(
            "Unable to build URLs outside an active request"
            " without 'SERVER_NAME' configured. Also configure"
            " 'APPLICATION_ROOT' and 'PREFERRED_URL_SCHEME' as"
            " needed."
        )
        _l_(9122)

    # When outside a request, generate a URL with scheme and
    # domain by default.
    if _external is None:
        _l_(9125)

        _external = True
        _l_(9124)
if _scheme is not None and not _external:
    _l_(9128)

    raise ValueError("When specifying '_scheme', '_external' must be True.")
    _l_(9127)

self.inject_url_defaults(endpoint, values)
_l_(9129)

try:
    _l_(9134)

    rv = url_adapter.build(  # type: ignore[union-attr]
        endpoint,
        values,
        method=_method,
        url_scheme=_scheme,
        force_external=_external,
    )
    _l_(9130)
except BuildError as error:
    _l_(9133)

    values.update(
        _anchor=_anchor, _method=_method, _scheme=_scheme, _external=_external
    )
    _l_(9131)
    aux = self.handle_url_build_error(error, endpoint, values)
    _l_(9132)
    exit(aux)

if _anchor is not None:
    _l_(9136)

    rv = f"{rv}#{url_quote(_anchor)}"
    _l_(9135)
aux = rv
_l_(9137)

exit(aux)
