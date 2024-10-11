# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: adding a new column to a DataFrame from an existing column/series
# -> always already takes a copy on assignment
# (no change in behaviour here)
# TODO can we achieve the same behaviour with Copy-on-Write?
df = DataFrame({"a": [1, 2, 3], "b": [0.1, 0.2, 0.3]})

s = Series([10, 11, 12])
df["new"] = s
assert not np.shares_memory(get_array(df, "new"), s.values)

# editing series -> doesn't modify column in frame
s[0] = 0
expected = DataFrame({"a": [1, 2, 3], "b": [0.1, 0.2, 0.3], "new": [10, 11, 12]})
tm.assert_frame_equal(df, expected)

# editing column in frame -> doesn't modify series
df.loc[2, "new"] = 100
expected_s = Series([0, 11, 12])
tm.assert_series_equal(s, expected_s)
