# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
df = DataFrame(
    {
        "key1": get_test_data(),
        "key2": get_test_data(),
        "data1": np.random.randn(50),
        "data2": np.random.randn(50),
    }
)

# exclude a couple keys for fun
df = df[df["key2"] > 1]
exit(df)
