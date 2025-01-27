# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# GH#24704
a1 = Series([0, np.nan, 4], name="a")
a2 = Series([np.nan, 3, 5], name="a")
df = concat([a1, a2], axis=1)

result = df.astype(dtype)
expected = concat([a1.astype(dtype), a2.astype(dtype)], axis=1)
tm.assert_frame_equal(result, expected)
