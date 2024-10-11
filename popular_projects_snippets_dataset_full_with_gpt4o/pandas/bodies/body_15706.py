# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_compare.py
# We want to make sure two NaNs are considered the same
# and dropped where applicable
s1 = pd.Series(["a", "b", np.nan])
s2 = pd.Series(["x", "b", np.nan])

result = s1.compare(s2)
expected = pd.DataFrame([["a", "x"]], columns=["self", "other"])
tm.assert_frame_equal(result, expected)
