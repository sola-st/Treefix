# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(
    ["a_b", np.nan, "asdf_cas_asdf", True, datetime.today(), "foo", None, 1, 2.0]
)
result = ser.str.split("_").str.join("_")
expected = Series(
    ["a_b", np.nan, "asdf_cas_asdf", np.nan, np.nan, "foo", np.nan, np.nan, np.nan]
)
tm.assert_series_equal(result, expected)
