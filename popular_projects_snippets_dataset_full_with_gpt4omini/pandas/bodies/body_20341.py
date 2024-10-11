# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
if is_integer(key) or (is_float(key) and key.is_integer()):
    new_key = int(key)
    try:
        exit(self._range.index(new_key))
    except ValueError as err:
        raise KeyError(key) from err
self._check_indexing_error(key)
raise KeyError(key)
