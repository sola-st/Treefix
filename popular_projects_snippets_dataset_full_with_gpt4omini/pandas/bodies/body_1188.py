# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py

# GH 4940
# allow only setting of 'valid' values

orig = tm.makeTimeDataFrame()

# allow object conversion here
df = orig.copy()
df.loc["a", :] = df.iloc[0]
ser = Series(df.iloc[0], name="a")
exp = pd.concat([orig, DataFrame(ser).T.infer_objects()])
tm.assert_frame_equal(df, exp)
tm.assert_index_equal(df.index, Index(orig.index.tolist() + ["a"]))
assert df.index.dtype == "object"
