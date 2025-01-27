# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_partial.py
frame = multiindex_dataframe_random_data
expected = frame.copy()
result = frame.copy()
result.loc[["foo", "bar"]] = 0
expected.loc["foo"] = 0
expected.loc["bar"] = 0
tm.assert_frame_equal(result, expected)

expected = frame.copy()
result = frame.copy()
result.loc["foo":"bar"] = 0
expected.loc["foo"] = 0
expected.loc["bar"] = 0
tm.assert_frame_equal(result, expected)

expected = frame["A"].copy()
result = frame["A"].copy()
result.loc[["foo", "bar"]] = 0
expected.loc["foo"] = 0
expected.loc["bar"] = 0
tm.assert_series_equal(result, expected)

expected = frame["A"].copy()
result = frame["A"].copy()
result.loc["foo":"bar"] = 0
expected.loc["foo"] = 0
expected.loc["bar"] = 0
tm.assert_series_equal(result, expected)
