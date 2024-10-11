# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_update.py
s = Series([1.5, np.nan, 3.0, 4.0, np.nan])
s2 = Series([np.nan, 3.5, np.nan, 5.0])
s.update(s2)

expected = Series([1.5, 3.5, 3.0, 5.0, np.nan])
tm.assert_series_equal(s, expected)

# GH 3217
df = DataFrame([{"a": 1}, {"a": 3, "b": 2}])
df["c"] = np.nan
df_orig = df.copy()

df["c"].update(Series(["foo"], index=[0]))
if using_copy_on_write:
    expected = df_orig
else:
    expected = DataFrame(
        [[1, np.nan, "foo"], [3, 2.0, np.nan]], columns=["a", "b", "c"]
    )
tm.assert_frame_equal(df, expected)
