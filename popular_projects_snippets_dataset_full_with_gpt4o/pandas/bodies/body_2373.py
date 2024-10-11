# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_set_value.py
df_orig = DataFrame(np.random.randn(3, 3), index=range(3), columns=list("ABC"))

# this is actually ambiguous as the 2 is interpreted as a positional
# so column is not created
df = df_orig.copy()
df._set_value("C", 2, 1.0)
assert list(df.index) == list(df_orig.index) + ["C"]
# assert list(df.columns) == list(df_orig.columns) + [2]

df = df_orig.copy()
df.loc["C", 2] = 1.0
assert list(df.index) == list(df_orig.index) + ["C"]
# assert list(df.columns) == list(df_orig.columns) + [2]

# create both new
df = df_orig.copy()
df._set_value("C", "D", 1.0)
assert list(df.index) == list(df_orig.index) + ["C"]
assert list(df.columns) == list(df_orig.columns) + ["D"]

df = df_orig.copy()
df.loc["C", "D"] = 1.0
assert list(df.index) == list(df_orig.index) + ["C"]
assert list(df.columns) == list(df_orig.columns) + ["D"]
