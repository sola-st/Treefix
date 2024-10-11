# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_period.py
arr = period_array(["2000", "2001"] * 500, freq="D")
result = str(arr)
expected = (
    "<PeriodArray>\n"
    "['2000-01-01', '2001-01-01', '2000-01-01', '2001-01-01', "
    "'2000-01-01',\n"
    " '2001-01-01', '2000-01-01', '2001-01-01', '2000-01-01', "
    "'2001-01-01',\n"
    " ...\n"
    " '2000-01-01', '2001-01-01', '2000-01-01', '2001-01-01', "
    "'2000-01-01',\n"
    " '2001-01-01', '2000-01-01', '2001-01-01', '2000-01-01', "
    "'2001-01-01']\n"
    "Length: 1000, dtype: period[D]"
)
assert result == expected
