# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
df = pd.DataFrame({"a": ["a", None, "b"]})
tm.assert_frame_equal(df + df, pd.DataFrame({"a": ["aa", np.nan, "bb"]}))
