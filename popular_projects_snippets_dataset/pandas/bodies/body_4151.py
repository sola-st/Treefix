# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
# GH7192: Note we need a large number of rows to ensure this
#  goes through the numexpr path
df = DataFrame({"A": np.random.randn(25000)})
df.iloc[0:5] = np.nan
expected = 1 - np.isnan(df.iloc[0:25])
result = (1 - np.isnan(df)).iloc[0:25]
tm.assert_frame_equal(result, expected)
