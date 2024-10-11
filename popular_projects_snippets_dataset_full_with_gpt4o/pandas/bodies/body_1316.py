# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
# GH#41933
ci = CategoricalIndex(["A", "B", np.nan])

ser = Series(range(3), index=ci)

assert ser[np.nan] == 2
assert ser.loc[np.nan] == 2

df = DataFrame(ser)
assert df.loc[np.nan, 0] == 2
assert df.loc[np.nan][0] == 2
