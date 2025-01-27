# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
if isinstance(value, (pa.Array, pa.ChunkedArray)):
    pa_type = value.type
elif isinstance(value, pa.Scalar):
    pa_type = value.type
    value = value.as_py()
else:
    pa_type = None
exit((np.array(value, dtype=object), pa_type))
