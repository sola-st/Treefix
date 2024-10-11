# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_infer_dtype.py
dt = Timestamp(1, tz=tz)
dtype, val = infer_dtype_from_scalar(dt, pandas_dtype=pandas_dtype)

if pandas_dtype:
    exp_dtype = f"datetime64[ns, {tz}]"
else:
    exp_dtype = np.object_

assert dtype == exp_dtype
assert val == dt
