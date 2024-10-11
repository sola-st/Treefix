# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH 21521
df = DataFrame([[np.nan]])
result = getattr(df.groupby(**{key: val}), func)()
expected = df

tm.assert_frame_equal(result, expected)
