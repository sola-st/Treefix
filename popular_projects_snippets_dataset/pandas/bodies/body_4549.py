# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
obj = constructor(pd.NaT, dtype=dtype)
assert np.all(obj.dtypes == dtype)
assert np.all(obj.isna())
