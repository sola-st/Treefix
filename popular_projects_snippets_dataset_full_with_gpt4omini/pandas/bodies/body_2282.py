# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_mask.py
# GH#3733
df = DataFrame(data=np.random.randn(100, 50))
df = df.where(df > 0)  # create nans
bools = df > 0
mask = isna(df)
expected = bools.astype(object).mask(mask)
result = bools.mask(mask)
tm.assert_frame_equal(result, expected)
