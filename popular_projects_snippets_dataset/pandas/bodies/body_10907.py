# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_indexing.py
# Test the multiindex mentioned as the use-case in the documentation
df = _make_df_from_data(multiindex_data)
result = df.groupby("Date", as_index=False).nth(slice(3, -3))

sliced = {date: multiindex_data[date][3:-3] for date in multiindex_data}
expected = _make_df_from_data(sliced)

tm.assert_frame_equal(result, expected)
