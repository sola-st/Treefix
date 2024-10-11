# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
# see gh-11718
exp_name = "x"
exp_data = [NaT] * 2

if is_datetime64_any_dtype(value.dtype) and "plus" in op_name:
    expected = DatetimeIndex(exp_data, tz=value.tz, name=exp_name)
else:
    expected = TimedeltaIndex(exp_data, name=exp_name)

if not isinstance(value, Index):
    expected = expected.array

op = _ops[op_name]
result = op(NaT, value)
tm.assert_equal(result, expected)
