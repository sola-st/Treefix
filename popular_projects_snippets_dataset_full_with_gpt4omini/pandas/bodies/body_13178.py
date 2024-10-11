# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py

# supported in >= 0.7.0
df = pd.DataFrame()
df["a"] = pd.Categorical(list("abcdef"))

# test for null, out-of-order values, and unobserved category
df["b"] = pd.Categorical(
    ["bar", "foo", "foo", "bar", None, "bar"],
    dtype=pd.CategoricalDtype(["foo", "bar", "baz"]),
)

# test for ordered flag
df["c"] = pd.Categorical(
    ["a", "b", "c", "a", "c", "b"], categories=["b", "c", "d"], ordered=True
)

check_round_trip(df, pa)
