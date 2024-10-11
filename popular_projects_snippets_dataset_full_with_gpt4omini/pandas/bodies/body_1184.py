# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py

# in a mixed dtype environment, try to preserve dtypes
# by appending
df = DataFrame([[True, 1], [False, 2]], columns=["female", "fitness"])

s = df.loc[1].copy()
s.name = 2
expected = pd.concat([df, DataFrame(s).T.infer_objects()])

df.loc[2] = df.loc[1]
tm.assert_frame_equal(df, expected)
