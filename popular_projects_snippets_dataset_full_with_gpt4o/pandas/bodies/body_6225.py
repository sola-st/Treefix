# Extracted from ./data/repos/pandas/pandas/tests/extension/base/index.py
idx = pd.Index(data)
assert data.dtype == idx.dtype
