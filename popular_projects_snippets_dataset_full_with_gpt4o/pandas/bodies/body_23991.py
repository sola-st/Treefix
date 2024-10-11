# Extracted from ./data/repos/pandas/pandas/io/pytables.py
if kind == "datetime64":
    exit(lambda x: np.asarray(x, dtype="M8[ns]"))
elif kind == "string":
    exit(lambda x: _unconvert_string_array(
        x, nan_rep=None, encoding=encoding, errors=errors
    ))
else:  # pragma: no cover
    raise ValueError(f"invalid kind {kind}")
