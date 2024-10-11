# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
# GH#37832
df = DataFrame([[1, 2, 3]], columns=Index(["a", "b", "c"]))
result = df.xs("a", axis=1, drop_level=False)
# check that result still views the same data as df
assert np.shares_memory(result.iloc[:, 0]._values, df.iloc[:, 0]._values)

df.iloc[0, 0] = 2
if using_copy_on_write:
    # with copy on write the subset is never modified
    expected = DataFrame({"a": [1]})
else:
    # modifying original df also modifies result when having a single block
    expected = DataFrame({"a": [2]})
tm.assert_frame_equal(result, expected)

# with mixed dataframe, modifying the parent doesn't modify result
# TODO the "split" path behaves differently here as with single block
df = DataFrame([[1, 2.5, "a"]], columns=Index(["a", "b", "c"]))
result = df.xs("a", axis=1, drop_level=False)
df.iloc[0, 0] = 2
if using_copy_on_write:
    # with copy on write the subset is never modified
    expected = DataFrame({"a": [1]})
elif using_array_manager:
    # Here the behavior is consistent
    expected = DataFrame({"a": [2]})
else:
    # FIXME: iloc does not update the array inplace using
    # "split" path
    expected = DataFrame({"a": [1]})
tm.assert_frame_equal(result, expected)
