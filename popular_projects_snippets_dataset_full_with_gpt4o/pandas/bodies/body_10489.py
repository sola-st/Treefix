# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_filters.py
df = DataFrame(
    [
        ["best", "a", "x"],
        ["worst", "b", "y"],
        ["best", "c", "x"],
        ["best", "d", "y"],
        ["worst", "d", "y"],
        ["worst", "d", "y"],
        ["best", "d", "z"],
    ],
    columns=["a", "b", "c"],
)
with pytest.raises(TypeError, match="filter function returned a.*"):
    df.groupby("c").filter(lambda g: g["a"] == "best")
