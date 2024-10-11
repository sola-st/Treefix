import os # pragma: no cover
import json # pragma: no cover

prefix = 'FLASK' # pragma: no cover
loads = json.loads # pragma: no cover
self = {} # pragma: no cover
os.environ['NONFLASK_KEY'] = 'unrelated_value' # pragma: no cover
os.environ['FLASK_SIMPLE_KEY'] = '"simple_value"' # pragma: no cover

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
_l_(20393)
len_prefix = len(prefix)
_l_(20394)

for key in sorted(os.environ):
    _l_(20413)

    if not key.startswith(prefix):
        _l_(20396)

        continue
        _l_(20395)

    value = os.environ[key]
    _l_(20397)

    try:
        _l_(20401)

        value = loads(value)
        _l_(20398)
    except Exception:
        _l_(20400)

        # Keep the value as a string if loading failed.
        pass
        _l_(20399)

    # Change to key.removeprefix(prefix) on Python >= 3.9.
    key = key[len_prefix:]
    _l_(20402)

    if "__" not in key:
        _l_(20405)

        # A non-nested key, set directly.
        self[key] = value
        _l_(20403)
        continue
        _l_(20404)

    # Traverse nested dictionaries with keys separated by "__".
    current = self
    _l_(20406)
    *parts, tail = key.split("__")
    _l_(20407)

    for part in parts:
        _l_(20411)

        # If an intermediate dict does not exist, create it.
        if part not in current:
            _l_(20409)

            current[part] = {}
            _l_(20408)

        current = current[part]
        _l_(20410)

    current[tail] = value
    _l_(20412)
aux = True
_l_(20414)

exit(aux)
