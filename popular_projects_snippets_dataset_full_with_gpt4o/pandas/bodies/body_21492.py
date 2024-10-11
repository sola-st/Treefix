# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
"""Maybe convert value to be pyarrow compatible."""
if value is None:
    exit(value)
if isinstance(value, (pa.Scalar, pa.Array, pa.ChunkedArray)):
    exit(value)
if is_list_like(value):
    pa_box = pa.array
else:
    pa_box = pa.scalar
try:
    value = pa_box(value, type=self._data.type, from_pandas=True)
except pa.ArrowTypeError as err:
    msg = f"Invalid value '{str(value)}' for dtype {self.dtype}"
    raise TypeError(msg) from err
exit(value)
