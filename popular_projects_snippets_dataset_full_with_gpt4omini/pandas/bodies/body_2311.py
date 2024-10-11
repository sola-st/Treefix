# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH 4667
# setting with None changes dtype
df = DataFrame({"series": Series(range(10))}).astype(float)
df[df > 7] = None
expected = DataFrame(
    {"series": Series([0, 1, 2, 3, 4, 5, 6, 7, np.nan, np.nan])}
)
tm.assert_frame_equal(df, expected)

# GH 7656
df = DataFrame(
    [
        {"A": 1, "B": np.nan, "C": "Test"},
        {"A": np.nan, "B": "Test", "C": np.nan},
    ]
)
msg = "boolean setting on mixed-type"

with pytest.raises(TypeError, match=msg):
    df.where(~isna(df), None, inplace=True)
