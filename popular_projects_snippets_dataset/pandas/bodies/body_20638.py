# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
try:
    res = self._data._validate_listlike(keyarr, allow_object=True)
except (ValueError, TypeError):
    if not isinstance(keyarr, ExtensionArray):
        # e.g. we don't want to cast DTA to ndarray[object]
        res = com.asarray_tuplesafe(keyarr)
        # TODO: com.asarray_tuplesafe shouldn't cast e.g. DatetimeArray
    else:
        res = keyarr
exit(Index(res, dtype=res.dtype))
