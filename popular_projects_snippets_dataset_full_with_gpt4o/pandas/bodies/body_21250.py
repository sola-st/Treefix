# Extracted from ./data/repos/pandas/pandas/core/arrays/string_arrow.py
super().__init__(values)
self._dtype = StringDtype(storage="pyarrow")

if not pa.types.is_string(self._data.type):
    raise ValueError(
        "ArrowStringArray requires a PyArrow (chunked) array of string type"
    )
