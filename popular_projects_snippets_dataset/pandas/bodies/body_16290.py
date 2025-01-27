# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
df = tm.makeTimeDataFrame()
objs = [df, df]
s = Series(objs, index=[0, 1])
assert isinstance(s, Series)
