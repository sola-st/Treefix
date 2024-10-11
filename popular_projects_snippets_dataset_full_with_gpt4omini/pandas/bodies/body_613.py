# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_construct_from_scalar.py
# check we dont lose nanoseconds
td = Timedelta(1)
res = construct_1d_arraylike_from_scalar(td, 2, np.dtype("m8[ns]"))
assert res[0] == td
