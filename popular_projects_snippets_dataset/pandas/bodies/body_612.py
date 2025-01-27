# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_construct_from_scalar.py
# check we dont lose nanoseconds
ts = fixed_now_ts + Timedelta(1)
res = construct_1d_arraylike_from_scalar(ts, 2, np.dtype("M8[ns]"))
assert res[0] == ts
