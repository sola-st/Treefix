# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# scalar that won't fit in nanosecond dt64, but will fit in microsecond
scalar = datetime(9999, 1, 1)
exp_dtype = "M8[us]"  # pydatetime objects default to this reso
if cls is np.datetime64:
    scalar = np.datetime64(scalar, "D")
    exp_dtype = "M8[s]"  # closest reso to input
result = constructor(scalar)

item = get1(result)
dtype = result.dtype if isinstance(result, Series) else result.dtypes.iloc[0]

assert type(item) is Timestamp
assert item.asm8.dtype == exp_dtype
assert dtype == exp_dtype
