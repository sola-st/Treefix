# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# Check for the warning that is raised when the mode
# results cannot be sorted

df = DataFrame({"A": [np.nan, np.nan, "a", "a"]})
expected = DataFrame({"A": ["a", np.nan]})

with tm.assert_produces_warning(UserWarning):
    result = df.mode(dropna=False)
    result = result.sort_values(by="A").reset_index(drop=True)

tm.assert_frame_equal(result, expected)
