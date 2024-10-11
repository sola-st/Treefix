# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
if pa_version_under6p0:
    msg = "pyarrow>=6.0.0 is required for PyArrow backed ArrowExtensionArray."
    raise ImportError(msg)
if isinstance(values, pa.Array):
    self._data = pa.chunked_array([values])
elif isinstance(values, pa.ChunkedArray):
    self._data = values
else:
    raise ValueError(
        f"Unsupported type '{type(values)}' for ArrowExtensionArray"
    )
self._dtype = ArrowDtype(self._data.type)
