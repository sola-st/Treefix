# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# Check for the warning that is raised when the mode
# results cannot be sorted

expected = Series(["foo", np.nan])
s = Series([1, "foo", "foo", np.nan, np.nan])

with tm.assert_produces_warning(UserWarning):
    result = s.mode(dropna=False)
    result = result.sort_values().reset_index(drop=True)

tm.assert_series_equal(result, expected)
