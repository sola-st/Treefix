# Extracted from ./data/repos/pandas/pandas/io/pytables.py
assert data is not None
assert self.dtype is None

data, dtype_name = _get_data_and_dtype_name(data)

self.data = data
self.dtype = dtype_name
self.kind = _dtype_to_kind(dtype_name)
