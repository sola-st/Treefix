# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# datetime64 dtype
op = comparison_op
dti = date_range("1949-06-07 03:00:00", freq="H", periods=5, name=names[0])
ser = Series(dti).rename(names[1])
result = op(ser, dti)
assert result.name == names[2]

# datetime64tz dtype
dti = dti.tz_localize("US/Central")
dti = pd.DatetimeIndex(dti, freq="infer")  # freq not preserved by tz_localize
ser = Series(dti).rename(names[1])
result = op(ser, dti)
assert result.name == names[2]

# timedelta64 dtype
tdi = dti - dti.shift(1)
ser = Series(tdi).rename(names[1])
result = op(ser, tdi)
assert result.name == names[2]

# interval dtype
if op in [operator.eq, operator.ne]:
    # interval dtype comparisons not yet implemented
    ii = pd.interval_range(start=0, periods=5, name=names[0])
    ser = Series(ii).rename(names[1])
    result = op(ser, ii)
    assert result.name == names[2]

# categorical
if op in [operator.eq, operator.ne]:
    # categorical dtype comparisons raise for inequalities
    cidx = tdi.astype("category")
    ser = Series(cidx).rename(names[1])
    result = op(ser, cidx)
    assert result.name == names[2]
