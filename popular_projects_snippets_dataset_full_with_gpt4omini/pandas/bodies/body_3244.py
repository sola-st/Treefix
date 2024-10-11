# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_nlargest.py
# GH#43060
df = pd.DataFrame([np.nan, np.nan, 0, 1, 2, 3])
result = df.nlargest(5, 0)
expected = df.sort_values(0, ascending=False).head(5)
tm.assert_frame_equal(result, expected)
