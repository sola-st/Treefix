# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_month.py
# https://github.com/pandas-dev/pandas/issues/34580
offset, cases = case
shift = DatetimeIndex(cases.keys())
exp = DatetimeIndex(cases.values())

with tm.assert_produces_warning(None):
    # GH#22535 check that we don't get a FutureWarning from adding
    # an integer array to PeriodIndex
    result = offset + shift
tm.assert_index_equal(result, exp)
