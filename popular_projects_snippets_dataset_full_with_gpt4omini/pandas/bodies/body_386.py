# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
# do not parse freq-like string as period dtype
assert com.pandas_dtype("U") == np.dtype("U")
assert com.pandas_dtype("S") == np.dtype("S")
