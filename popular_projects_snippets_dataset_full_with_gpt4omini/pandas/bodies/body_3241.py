# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_nlargest.py
# GH#13412

df = df_duplicates
result = df.nsmallest(n, order)
expected = df.sort_values(order).head(n)
tm.assert_frame_equal(result, expected)

result = df.nlargest(n, order)
expected = df.sort_values(order, ascending=False).head(n)
tm.assert_frame_equal(result, expected)
