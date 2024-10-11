# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
assert not is_scalar(arr)
assert not is_scalar(MockNumpyLikeArray(arr))
