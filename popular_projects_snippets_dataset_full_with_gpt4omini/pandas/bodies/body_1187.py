# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
# GH#4940 inserting non-strings
orig = tm.makeTimeDataFrame()
df = orig.copy()

df.loc[key, :] = df.iloc[0]
ex_index = Index(list(orig.index) + [key], dtype=object, name=orig.index.name)
ex_data = np.concatenate([orig.values, df.iloc[[0]].values], axis=0)
expected = DataFrame(ex_data, index=ex_index, columns=orig.columns)

tm.assert_frame_equal(df, expected)
