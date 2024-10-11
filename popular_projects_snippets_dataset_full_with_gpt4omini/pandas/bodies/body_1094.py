# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
frame = multiindex_dataframe_random_data.T
expected = frame
df = frame.copy()
if using_copy_on_write:
    df["foo"]["one"] = 2
else:
    msg = "A value is trying to be set on a copy of a slice from a DataFrame"
    with pytest.raises(SettingWithCopyError, match=msg):
        df["foo"]["one"] = 2

result = df
tm.assert_frame_equal(result, expected)
