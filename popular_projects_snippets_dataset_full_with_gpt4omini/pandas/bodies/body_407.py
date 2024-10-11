# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
# GH 15585
assert not com.is_string_dtype(pd.Series(data))
