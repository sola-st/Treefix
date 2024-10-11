# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
# this is a copy in 0.14
df = multiindex_dataframe_random_data
df_orig = df.copy()
result = df.xs("two", level="second")

if using_copy_on_write:
    result[:] = 10
else:
    # setting this will give a SettingWithCopyError
    # as we are trying to write a view
    msg = "A value is trying to be set on a copy of a slice from a DataFrame"
    with pytest.raises(SettingWithCopyError, match=msg):
        result[:] = 10
tm.assert_frame_equal(df, df_orig)
