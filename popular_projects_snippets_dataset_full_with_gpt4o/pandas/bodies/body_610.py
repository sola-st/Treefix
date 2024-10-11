# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_infer_datetimelike.py
# see gh-19671.
result = Series(["M1701", Timestamp("20130101")])
assert result.dtype.kind == "O"
