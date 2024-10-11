# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
# GH#36527 empty frame has None index.name -> not retained
df = DataFrame()
series = Series(1.23, index=pd.RangeIndex(4, name="series_index"))
df["series"] = series
expected = DataFrame(
    {"series": [1.23] * 4}, index=pd.RangeIndex(4, name="series_index")
)
tm.assert_frame_equal(df, expected)
