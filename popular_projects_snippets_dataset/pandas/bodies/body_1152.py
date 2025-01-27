# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH 20951

df = DataFrame(
    {
        "A": [100, 100, 200, 200, 300, 300],
        "B": [10, 10, 20, 21, 31, 33],
        "C": range(6),
    }
)
df = df.set_index(["A", "B"])
with pytest.raises(KeyError, match="^1$"):
    df.loc[(100, 1)]
