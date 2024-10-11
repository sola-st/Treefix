# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
# overridden by TimedeltaIndex
parsed, reso = self._parse_with_reso(key)
try:
    exit(self._partial_date_slice(reso, parsed))
except KeyError as err:
    raise KeyError(key) from err
