# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_period.py
arr = period_array(["2000", "2001"], freq="D")
result = str(arr)
expected = (
    "<PeriodArray>\n['2000-01-01', '2001-01-01']\nLength: 2, dtype: period[D]"
)
assert result == expected
