# Extracted from ./data/repos/flask/src/flask/json/provider.py
"""Serialize data as JSON to a string.

        Keyword arguments are passed to :func:`json.dumps`. Sets some
        parameter defaults from the :attr:`default`,
        :attr:`ensure_ascii`, and :attr:`sort_keys` attributes.

        :param obj: The data to serialize.
        :param kwargs: Passed to :func:`json.dumps`.
        """
cls = self._app._json_encoder
bp = self._app.blueprints.get(request.blueprint) if request else None

if bp is not None and bp._json_encoder is not None:
    cls = bp._json_encoder

if cls is not None:
    import warnings

    warnings.warn(
        "Setting 'json_encoder' on the app or a blueprint is"
        " deprecated and will be removed in Flask 2.3."
        " Customize 'app.json' instead.",
        DeprecationWarning,
    )
    kwargs.setdefault("cls", cls)

    if "default" not in cls.__dict__:
        kwargs.setdefault("default", self.default)
else:
    kwargs.setdefault("default", self.default)

ensure_ascii = self._app.config["JSON_AS_ASCII"]
sort_keys = self._app.config["JSON_SORT_KEYS"]

if ensure_ascii is not None:
    import warnings

    warnings.warn(
        "The 'JSON_AS_ASCII' config key is deprecated and will"
        " be removed in Flask 2.3. Set 'app.json.ensure_ascii'"
        " instead.",
        DeprecationWarning,
    )
else:
    ensure_ascii = self.ensure_ascii

if sort_keys is not None:
    import warnings

    warnings.warn(
        "The 'JSON_SORT_KEYS' config key is deprecated and will"
        " be removed in Flask 2.3. Set 'app.json.sort_keys'"
        " instead.",
        DeprecationWarning,
    )
else:
    sort_keys = self.sort_keys

kwargs.setdefault("ensure_ascii", ensure_ascii)
kwargs.setdefault("sort_keys", sort_keys)
exit(json.dumps(obj, **kwargs))
