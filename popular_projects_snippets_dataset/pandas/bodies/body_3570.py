# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
frame = multiindex_dataframe_random_data

df = frame.copy()
df.index = np.arange(len(df))

# axis=1

# series
a_sorted = frame["A"].sort_index(level=0)

# preserve names
assert a_sorted.index.names == frame.index.names

# inplace
rs = frame.copy()
return_value = rs.sort_index(level=0, inplace=True)
assert return_value is None
tm.assert_frame_equal(rs, frame.sort_index(level=0))
