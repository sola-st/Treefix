# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
frame = multiindex_dataframe_random_data
df = frame.T.copy()
values = df.values

result = df[df > 0]
expected = df.where(df > 0)
tm.assert_frame_equal(result, expected)

df[df > 0] = 5
values[values > 0] = 5
tm.assert_almost_equal(df.values, values)

df[df == 5] = 0
values[values == 5] = 0
tm.assert_almost_equal(df.values, values)

# a df that needs alignment first
df[df[:-1] < 0] = 2
np.putmask(values[:-1], values[:-1] < 0, 2)
tm.assert_almost_equal(df.values, values)

with pytest.raises(TypeError, match="boolean values only"):
    df[df * 0] = 2
