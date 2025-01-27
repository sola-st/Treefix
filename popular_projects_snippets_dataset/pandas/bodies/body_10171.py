# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH: 34617
df = DataFrame(
    {
        "a": to_datetime(["2020-06-01 12:00", "2020-06-01 14:00", np.nan]),
        "b": [1, 2, 3],
        "c": [1, 1, 1],
    }
)
if key == "index":
    df = df.set_index("a")
with pytest.raises(ValueError, match=f"{key} values must not have NaT"):
    df.groupby("c").rolling("60min", **rollings)
