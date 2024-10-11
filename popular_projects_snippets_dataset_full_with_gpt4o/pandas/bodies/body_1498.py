# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#6252 setting with an empty frame
keys1 = ["@" + str(i) for i in range(5)]
val1 = np.arange(5, dtype="int64")

keys2 = ["@" + str(i) for i in range(4)]
val2 = np.arange(4, dtype="int64")

index = list(set(keys1).union(keys2))
df = DataFrame(index=index)
df["A"] = np.nan
df.loc[keys1, "A"] = val1

df["B"] = np.nan
df.loc[keys2, "B"] = val2

# Because df["A"] was initialized as float64, setting values into it
#  is inplace, so that dtype is retained
sera = Series(val1, index=keys1, dtype=np.float64)
serb = Series(val2, index=keys2)
expected = DataFrame({"A": sera, "B": serb}).reindex(index=index)
tm.assert_frame_equal(df, expected)
