# Extracted from ./data/repos/flask/src/flask/json/provider.py
"""Serialize the given arguments as JSON, and return a
        :class:`~flask.Response` object with it. The response mimetype
        will be "application/json" and can be changed with
        :attr:`mimetype`.

        If :attr:`compact` is ``False`` or debug mode is enabled, the
        output will be formatted to be easier to read.

        Either positional or keyword arguments can be given, not both.
        If no arguments are given, ``None`` is serialized.

        :param args: A single value to serialize, or multiple values to
            treat as a list to serialize.
        :param kwargs: Treat as a dict to serialize.
        """
obj = self._prepare_response_obj(args, kwargs)
dump_args: t.Dict[str, t.Any] = {}
pretty = self._app.config["JSONIFY_PRETTYPRINT_REGULAR"]
mimetype = self._app.config["JSONIFY_MIMETYPE"]

if pretty is not None:
    import warnings

    warnings.warn(
        "The 'JSONIFY_PRETTYPRINT_REGULAR' config key is"
        " deprecated and will be removed in Flask 2.3. Set"
        " 'app.json.compact' instead.",
        DeprecationWarning,
    )
    compact: bool | None = not pretty
else:
    compact = self.compact

if (compact is None and self._app.debug) or compact is False:
    dump_args.setdefault("indent", 2)
else:
    dump_args.setdefault("separators", (",", ":"))

if mimetype is not None:
    import warnings

    warnings.warn(
        "The 'JSONIFY_MIMETYPE' config key is deprecated and"
        " will be removed in Flask 2.3. Set 'app.json.mimetype'"
        " instead.",
        DeprecationWarning,
    )
else:
    mimetype = self.mimetype

exit(self._app.response_class(
    f"{self.dumps(obj, **dump_args)}\n", mimetype=mimetype
))
