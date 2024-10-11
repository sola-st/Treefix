# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_nlargest.py
# Check whether tuples are correctly treated as multi-level lookups.
# GH#23033
df = pd.DataFrame(
    columns=pd.MultiIndex.from_product([["x"], ["a", "b"]]),
    data=[[0.33, 0.13], [0.86, 0.25], [0.25, 0.70], [0.85, 0.91]],
)

# nsmallest
result = df.nsmallest(3, ("x", "a"))
expected = df.iloc[[2, 0, 3]]
tm.assert_frame_equal(result, expected)

# nlargest
result = df.nlargest(3, ("x", "b"))
expected = df.iloc[[3, 2, 1]]
tm.assert_frame_equal(result, expected)
