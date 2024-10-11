# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH#7261
klass = index_or_series
arg_op = "arg" + opname if klass is Index else "idx" + opname

obj = klass([NaT, datetime(2011, 11, 1)])
assert getattr(obj, arg_op)() == 1
result = getattr(obj, arg_op)(skipna=False)
if klass is Series:
    assert np.isnan(result)
else:
    assert result == -1

obj = klass([NaT, datetime(2011, 11, 1), NaT])
# check DatetimeIndex non-monotonic path
assert getattr(obj, arg_op)() == 1
result = getattr(obj, arg_op)(skipna=False)
if klass is Series:
    assert np.isnan(result)
else:
    assert result == -1
