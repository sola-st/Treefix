# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_rank.py
# GH#40518
fill_value = np.nan if use_nan else 3
df = DataFrame(
    [
        [-1, 1],
        [-1, 2],
        [1, fill_value],
        [-1, fill_value],
    ],
    columns=["group", "val"],
)
result = df.groupby(["group"])["val"].rank(
    method="dense",
    pct=True,
)
if use_nan:
    expected = Series([0.5, 1, np.nan, np.nan], name="val")
else:
    expected = Series([1 / 3, 2 / 3, 1, 1], name="val")

tm.assert_series_equal(result, expected)
