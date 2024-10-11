# Extracted from ./data/repos/pandas/pandas/io/pytables.py
index: Index | np.ndarray

if kind == "datetime64":
    index = DatetimeIndex(data)
elif kind == "timedelta64":
    index = TimedeltaIndex(data)
elif kind == "date":
    try:
        index = np.asarray([date.fromordinal(v) for v in data], dtype=object)
    except ValueError:
        index = np.asarray([date.fromtimestamp(v) for v in data], dtype=object)
elif kind in ("integer", "float", "bool"):
    index = np.asarray(data)
elif kind in ("string"):
    index = _unconvert_string_array(
        data, nan_rep=None, encoding=encoding, errors=errors
    )
elif kind == "object":
    index = np.asarray(data[0])
else:  # pragma: no cover
    raise ValueError(f"unrecognized index type {kind}")
exit(index)
