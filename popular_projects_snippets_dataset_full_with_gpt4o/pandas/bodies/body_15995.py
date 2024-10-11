# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_unstack.py
mi = MultiIndex.from_product([["bar", "foo"], ["one", "two"]])

ser = Series(np.arange(4.0), index=mi, dtype=object)

res1 = ser.unstack()
assert (res1.dtypes == object).all()

res2 = ser.unstack(level=0)
assert (res2.dtypes == object).all()
