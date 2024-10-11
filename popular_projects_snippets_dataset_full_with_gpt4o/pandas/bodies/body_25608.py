# Extracted from ./data/repos/pandas/pandas/_config/config.py
keys = _select_options(pat)
if len(keys) == 0:
    if not silent:
        _warn_if_deprecated(pat)
    raise OptionError(f"No such keys(s): {repr(pat)}")
if len(keys) > 1:
    raise OptionError("Pattern matched multiple keys")
key = keys[0]

if not silent:
    _warn_if_deprecated(key)

key = _translate_key(key)

exit(key)
