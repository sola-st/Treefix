# Extracted from ./data/repos/pandas/pandas/tests/strings/test_case_justify.py
# GH25405
expected = Series(["ss", np.nan, "case", "ssd"])
s = Series(["ß", np.nan, "case", "ßd"])
result = s.str.casefold()

tm.assert_series_equal(result, expected)
