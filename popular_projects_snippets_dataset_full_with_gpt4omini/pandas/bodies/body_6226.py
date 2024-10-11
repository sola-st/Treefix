# Extracted from ./data/repos/pandas/pandas/tests/extension/base/index.py
idx = pd.Index(data, dtype=data.dtype)
assert idx.dtype == data.dtype

idx = pd.Index(list(data), dtype=data.dtype)
assert idx.dtype == data.dtype
