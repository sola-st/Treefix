# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_infer_dtype.py
p = Period("2011-01-01", freq=freq)
dtype, val = infer_dtype_from_scalar(p, pandas_dtype=pandas_dtype)

if pandas_dtype:
    exp_dtype = f"period[{freq}]"
else:
    exp_dtype = np.object_

assert dtype == exp_dtype
assert val == p
