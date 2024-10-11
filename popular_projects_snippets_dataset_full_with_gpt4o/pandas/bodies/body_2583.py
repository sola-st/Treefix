# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py

# Test for issue #18582
df = float_frame.copy()
mask = mask_type(df)

# index with boolean mask
result = df.copy()
result[mask] = np.nan

expected = df.copy()
expected.values[np.array(mask)] = np.nan
tm.assert_frame_equal(result, expected)
