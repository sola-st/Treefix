# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#15686, duplicate columns and mixed dtype
df1 = DataFrame([{"A": None, "B": 1}, {"A": 2, "B": 2}])
df2 = DataFrame([{"A": 3, "B": 3}, {"A": 4, "B": 4}])
df = concat([df1, df2], axis=1)
df.iloc[0, 0] = -1

assert df.iloc[0, 0] == -1
assert df.iloc[0, 2] == 3
assert df.dtypes.iloc[2] == np.int64
