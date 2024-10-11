import os # pragma: no cover
import json # pragma: no cover

prefix = 'FLASK' # pragma: no cover
os.environ = {'FLASK_DEBUG': 'true', 'FLASK_ENV': 'development', 'FLASK_NESTED__KEY': 'value'} # pragma: no cover
loads = json.loads # pragma: no cover
self = type('Mock', (object,), {'__setitem__': lambda self, key, value: setattr(self, key, value)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/config.py
from l3.Runtime import _l_
"""Load any environment variables that start with ``FLASK_``,
        dropping the prefix from the env key for the config key. Values
        are passed through a loading function to attempt to convert them
        to more specific types than strings.

        Keys are loaded in :func:`sorted` order.

        The default loading function attempts to parse values as any
        valid JSON type, including dicts and lists.

        Specific items in nested dicts can be set by separating the
        keys with double underscores (``__``). If an intermediate key
        doesn't exist, it will be initialized to an empty dict.

        :param prefix: Load env vars that start with this prefix,
            separated with an underscore (``_``).
        :param loads: Pass each string value to this function and use
            the returned value as the config value. If any error is
            raised it is ignored and the value remains a string. The
            default is :func:`json.loads`.

        .. versionadded:: 2.1
        """
prefix = f"{prefix}_"
_l_(20427)
len_prefix = len(prefix)
_l_(20428)

for key in sorted(os.environ):
    _l_(20447)

    if not key.startswith(prefix):
        _l_(20430)

        continue
        _l_(20429)

    value = os.environ[key]
    _l_(20431)

    try:
        _l_(20435)

        value = loads(value)
        _l_(20432)
    except Exception:
        _l_(20434)

        # Keep the value as a string if loading failed.
        pass
        _l_(20433)

    # Change to key.removeprefix(prefix) on Python >= 3.9.
    key = key[len_prefix:]
    _l_(20436)

    if "__" not in key:
        _l_(20439)

        # A non-nested key, set directly.
        self[key] = value
        _l_(20437)
        continue
        _l_(20438)

    # Traverse nested dictionaries with keys separated by "__".
    current = self
    _l_(20440)
    *parts, tail = key.split("__")
    _l_(20441)

    for part in parts:
        _l_(20445)

        # If an intermediate dict does not exist, create it.
        if part not in current:
            _l_(20443)

            current[part] = {}
            _l_(20442)

        current = current[part]
        _l_(20444)

    current[tail] = value
    _l_(20446)
aux = True
_l_(20448)

exit(aux)
