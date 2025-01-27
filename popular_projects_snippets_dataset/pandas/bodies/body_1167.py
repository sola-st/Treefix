# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
# GH#31368 empty frame has non-None index.name -> retained
df = DataFrame({}, index=pd.RangeIndex(0, name="df_index"))
series = Series(1.23, index=pd.RangeIndex(4, name="series_index"))

df["series"] = series
expected = DataFrame(
    {"series": [1.23] * 4}, index=pd.RangeIndex(4, name="df_index")
)

tm.assert_frame_equal(df, expected)
