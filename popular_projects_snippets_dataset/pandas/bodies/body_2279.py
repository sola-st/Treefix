# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_mask.py
# GH#8801
df = DataFrame(np.random.randn(5, 3))
cond = df > 0

rdf = df.copy()

return_value = rdf.where(cond, inplace=True)
assert return_value is None
tm.assert_frame_equal(rdf, df.where(cond))
tm.assert_frame_equal(rdf, df.mask(~cond))

rdf = df.copy()
return_value = rdf.where(cond, -df, inplace=True)
assert return_value is None
tm.assert_frame_equal(rdf, df.where(cond, -df))
tm.assert_frame_equal(rdf, df.mask(~cond, -df))
