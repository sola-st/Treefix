# Extracted from ./data/repos/pandas/pandas/tests/strings/test_case_justify.py
s = Series(["om", np.nan, "nom", "nom"], dtype=any_string_dtype)

result = s.str.upper()
expected = Series(["OM", np.nan, "NOM", "NOM"], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)

result = result.str.lower()
tm.assert_series_equal(result, s)
