# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
# Case: converting a Series to a DataFrame with to_frame
ser = Series([1, 2, 3])
ser_orig = ser.copy()

df = ser[:].to_frame()

# currently this always returns a "view"
assert np.shares_memory(ser.values, get_array(df, 0))

df.iloc[0, 0] = 0

if using_copy_on_write:
    # mutating df triggers a copy-on-write for that column
    assert not np.shares_memory(ser.values, get_array(df, 0))
    tm.assert_series_equal(ser, ser_orig)
else:
    # but currently select_dtypes() actually returns a view -> mutates parent
    expected = ser_orig.copy()
    expected.iloc[0] = 0
    tm.assert_series_equal(ser, expected)

# modify original series -> don't modify dataframe
df = ser[:].to_frame()
ser.iloc[0] = 0

if using_copy_on_write:
    tm.assert_frame_equal(df, ser_orig.to_frame())
else:
    expected = ser_orig.copy().to_frame()
    expected.iloc[0, 0] = 0
    tm.assert_frame_equal(df, expected)
