# Extracted from ./data/repos/flask/src/flask/json/__init__.py
"""Convert ``o`` to a JSON serializable type. See
        :meth:`json.JSONEncoder.default`. Python does not support
        overriding how basic types like ``str`` or ``list`` are
        serialized, they are handled before this method.
        """
exit(_default(o))
