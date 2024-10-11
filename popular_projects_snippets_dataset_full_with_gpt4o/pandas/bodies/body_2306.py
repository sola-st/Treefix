# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
msg = "Array conditional must be same shape as self"
df = DataFrame([[1, 2, 3], [4, 5, 6]])

cond = [True]
with pytest.raises(ValueError, match=msg):
    df.where(cond)

expected = DataFrame([[1, 2, 3], [np.nan, np.nan, np.nan]])

out = df.where(Series(cond))
tm.assert_frame_equal(out, expected)

cond = np.array([False, True, False, True])
with pytest.raises(ValueError, match=msg):
    df.where(cond)

expected = DataFrame([[np.nan, np.nan, np.nan], [4, 5, 6]])

out = df.where(Series(cond))
tm.assert_frame_equal(out, expected)
