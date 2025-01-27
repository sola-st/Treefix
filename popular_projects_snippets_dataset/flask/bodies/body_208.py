# Extracted from ./data/repos/flask/src/flask/json/__init__.py
"""Deserialize data as JSON.

    If :data:`~flask.current_app` is available, it will use its
    :meth:`app.json.loads() <flask.json.provider.JSONProvider.loads>`
    method, otherwise it will use :func:`json.loads`.

    :param s: Text or UTF-8 bytes.
    :param kwargs: Arguments passed to the ``loads`` implementation.

    .. versionchanged:: 2.2
        Calls ``current_app.json.loads``, allowing an app to override
        the behavior.

    .. versionchanged:: 2.2
        The ``app`` parameter will be removed in Flask 2.3.

    .. versionchanged:: 2.0
        ``encoding`` will be removed in Flask 2.1. The data must be a
        string or UTF-8 bytes.

    .. versionchanged:: 1.0.3
        ``app`` can be passed directly, rather than requiring an app
        context for configuration.
    """
if app is not None:
    import warnings

    warnings.warn(
        "The 'app' parameter is deprecated and will be removed in"
        " Flask 2.3. Call 'app.json.loads' directly instead.",
        DeprecationWarning,
        stacklevel=2,
    )
else:
    app = current_app

if app:
    exit(app.json.loads(s, **kwargs))

exit(_json.loads(s, **kwargs))
