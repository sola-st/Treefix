# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
scalar = np.datetime64(np.iinfo(np.int64).max, "D")
result = constructor(scalar)
item = get1(result)
assert type(item) is np.datetime64
dtype = result.dtype if isinstance(result, Series) else result.dtypes.iloc[0]
assert dtype == object
