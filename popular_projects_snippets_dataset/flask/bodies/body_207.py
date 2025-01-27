# Extracted from ./data/repos/flask/src/flask/json/__init__.py
"""Serialize data as JSON and write to a file.

    If :data:`~flask.current_app` is available, it will use its
    :meth:`app.json.dump() <flask.json.provider.JSONProvider.dump>`
    method, otherwise it will use :func:`json.dump`.

    :param obj: The data to serialize.
    :param fp: A file opened for writing text. Should use the UTF-8
        encoding to be valid JSON.
    :param kwargs: Arguments passed to the ``dump`` implementation.

    .. versionchanged:: 2.2
        Calls ``current_app.json.dump``, allowing an app to override
        the behavior.

    .. versionchanged:: 2.2
        The ``app`` parameter will be removed in Flask 2.3.

    .. versionchanged:: 2.0
        Writing to a binary file, and the ``encoding`` argument, will be
        removed in Flask 2.1.
    """
if app is not None:
    import warnings

    warnings.warn(
        "The 'app' parameter is deprecated and will be removed in"
        " Flask 2.3. Call 'app.json.dump' directly instead.",
        DeprecationWarning,
        stacklevel=2,
    )
else:
    app = current_app

if app:
    app.json.dump(obj, fp, **kwargs)
else:
    kwargs.setdefault("default", _default)
    _json.dump(obj, fp, **kwargs)
