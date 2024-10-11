# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH#25438 don't cast df['a'] to float64
df = DataFrame({"a": [1, 2, 3, np.nan], "b": ["some", "strings", "here", "he"]})
df["a"] = df["a"].astype("Int64")

res = df.replace("", np.nan)
tm.assert_series_equal(res["a"], df["a"])
