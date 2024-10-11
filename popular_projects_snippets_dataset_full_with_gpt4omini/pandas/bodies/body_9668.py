# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_reductions.py
arr = period_array([], freq="D")
result = arr.min(skipna=skipna)
assert result is pd.NaT

result = arr.max(skipna=skipna)
assert result is pd.NaT
