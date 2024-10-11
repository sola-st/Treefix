# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py

# ~ 40000000 possible unique groups
key1 = tm.rands_array(10, 10000)
key1 = np.tile(key1, 2)
key2 = key1[::-1]

df = DataFrame({"key1": key1, "key2": key2, "value1": np.random.randn(20000)})

df2 = DataFrame(
    {"key1": key1[::2], "key2": key2[::2], "value2": np.random.randn(10000)}
)

# just to hit the label compression code path
merge(df, df2, how="outer")
