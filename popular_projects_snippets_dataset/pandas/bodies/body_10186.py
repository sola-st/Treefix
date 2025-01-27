# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 46061
df = DataFrame(
    {
        "A": [1] * 3 + [2] * 3,
        "B": [Timestamp(year, 1, 1) for year in [2020, 2021, 2019]] * 2,
        "C": range(6),
    }
)
with pytest.raises(ValueError, match="Each group within B must be monotonic."):
    df.groupby("A").rolling("365D", on="B")
