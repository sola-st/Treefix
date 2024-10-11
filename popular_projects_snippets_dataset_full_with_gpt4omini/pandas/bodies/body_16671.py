# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# #8596

df1 = DataFrame({"key": [1], "v1": [10]})
df2 = DataFrame({"key": [2], "v1": [20]})
df = merge(df1, df2, how="outer")
assert df["key"].dtype == "int64"

df1 = DataFrame({"key": [True], "v1": [1]})
df2 = DataFrame({"key": [False], "v1": [0]})
df = merge(df1, df2, how="outer")

# GH13169
# GH#40073
assert df["key"].dtype == "bool"

df1 = DataFrame({"val": [1]})
df2 = DataFrame({"val": [2]})
lkey = np.array([1])
rkey = np.array([2])
df = merge(df1, df2, left_on=lkey, right_on=rkey, how="outer")
assert df["key_0"].dtype == np.int_
