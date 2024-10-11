# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_period.py
arr = period_array(["2000", "2001", "2002"], freq="D")
result = arr.fillna(pd.Period("2000", "D"))
assert result is not arr
