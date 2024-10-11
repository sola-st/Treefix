# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
# GH#2200
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}).set_index(
    ["a", "b"]
)
index = list(df.index)
index[0] = ("faz", "boo")
df.index = index
repr(df)

# this travels an improper code path
index[0] = ["faz", "boo"]
df.index = index
repr(df)
