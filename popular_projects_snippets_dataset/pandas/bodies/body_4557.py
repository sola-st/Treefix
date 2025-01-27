# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
scalar = cls(np.iinfo(np.int64).max, "D")
result = constructor(scalar)
item = get1(result)
assert type(item) is cls
dtype = result.dtype if isinstance(result, Series) else result.dtypes.iloc[0]
assert dtype == object
