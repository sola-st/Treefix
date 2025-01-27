# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py

# GH3492
df = DataFrame(
    {"a": {1: "aaa", 2: "bbb", 3: "ccc"}, "b": {1: 111, 2: 222, 3: 333}}
)

# this works, new column is created correctly
df["test"] = df["a"].apply(lambda x: "_" if x == "aaa" else x)

# this does not work, ie column test is not changed
idx = df["test"] == "_"
temp = df.loc[idx, "a"].apply(lambda x: "-----" if x == "aaa" else x)
df.loc[idx, "test"] = temp
assert df.iloc[0, 2] == "-----"
