# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_month.py
offset, cases = case
shift = DatetimeIndex(cases.keys())

with tm.assert_produces_warning(None):
    # GH#22535 check that we don't get a FutureWarning from adding
    # an integer array to PeriodIndex
    result = offset + shift

exp = DatetimeIndex(cases.values())
tm.assert_index_equal(result, exp)
