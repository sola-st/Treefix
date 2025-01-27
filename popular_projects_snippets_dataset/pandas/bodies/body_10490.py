# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_filters.py
df = DataFrame(
    [
        ["best", "a", 1],
        ["worst", "b", 1],
        ["best", "c", 1],
        ["best", "d", 1],
        ["worst", "d", 1],
        ["worst", "d", 1],
        ["best", "d", 1],
    ],
    columns=["a", "b", "c"],
)
with pytest.raises(TypeError, match="filter function returned a.*"):
    df.groupby("a").filter(lambda g: g.c.mean())
