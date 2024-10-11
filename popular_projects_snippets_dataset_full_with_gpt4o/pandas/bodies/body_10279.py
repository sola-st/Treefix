# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_dropna.py
# GH 39895
df = pd.DataFrame([[np.nan, 0, 1]], columns=["a", "b", "c"])
df = df.set_index(["a", "b"])
result = df.groupby(["a", "b"], dropna=False).first()
expected = df
tm.assert_frame_equal(result, expected)
