# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# must be the same as dateutil result
exp_now = parse(date_str)

result1, _ = parsing.parse_datetime_string_with_reso(date_str)
with tm.assert_produces_warning(UserWarning, match="Could not infer format"):
    result2 = to_datetime(date_str)
    result3 = to_datetime([date_str])
result4 = Timestamp(date_str)
result5 = DatetimeIndex([date_str])[0]
# parse time string return time string based on default date
# others are not, and can't be changed because it is used in
# time series plot
assert result1 == exp_def
assert result2 == exp_now
assert result3 == exp_now
assert result4 == exp_now
assert result5 == exp_now
