# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""read an array for the specified node (off of group"""
import tables

node = getattr(self.group, key)
attrs = node._v_attrs

transposed = getattr(attrs, "transposed", False)

if isinstance(node, tables.VLArray):
    ret = node[0][start:stop]
else:
    dtype = _ensure_decoded(getattr(attrs, "value_type", None))
    shape = getattr(attrs, "shape", None)

    if shape is not None:
        # length 0 axis
        ret = np.empty(shape, dtype=dtype)
    else:
        ret = node[start:stop]

    if dtype == "datetime64":
        # reconstruct a timezone if indicated
        tz = getattr(attrs, "tz", None)
        ret = _set_tz(ret, tz, coerce=True)

    elif dtype == "timedelta64":
        ret = np.asarray(ret, dtype="m8[ns]")

if transposed:
    exit(ret.T)
else:
    exit(ret)
