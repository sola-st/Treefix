# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# scalar that won't fit in nanosecond td64, but will fit in microsecond
scalar = datetime(9999, 1, 1) - datetime(1970, 1, 1)
exp_dtype = "m8[us]"  # smallest reso that fits
if cls is np.timedelta64:
    scalar = np.timedelta64(scalar, "D")
    exp_dtype = "m8[s]"  # closest reso to input
result = constructor(scalar)

item = get1(result)
dtype = result.dtype if isinstance(result, Series) else result.dtypes.iloc[0]

assert type(item) is Timedelta
assert item.asm8.dtype == exp_dtype
assert dtype == exp_dtype
