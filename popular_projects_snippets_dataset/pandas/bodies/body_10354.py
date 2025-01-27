# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_index_as_string.py
df = pd.DataFrame(
    {
        "outer": ["a", "a", "a", "b", "b", "b"],
        "inner": [1, 2, 3, 1, 2, 3],
        "A": np.arange(6),
        "B": ["one", "one", "two", "two", "one", "one"],
    }
)
s = df.set_index(["outer", "inner", "B"])["A"]

exit(s)
