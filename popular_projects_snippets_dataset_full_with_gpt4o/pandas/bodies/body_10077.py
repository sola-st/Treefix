# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_functions.py
# GH12373

# Just testing that these don't throw exceptions and that
# the return type is float64. Other tests will cover quantitative
# correctness
result = DataFrame(np.arange(20, dtype=data_type)).rolling(window=5).max()
assert result.dtypes[0] == np.dtype("f8")
result = DataFrame(np.arange(20, dtype=data_type)).rolling(window=5).min()
assert result.dtypes[0] == np.dtype("f8")
