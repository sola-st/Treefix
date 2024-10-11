# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
idx = Index(arr)
assert idx.dtype == arr.dtype
