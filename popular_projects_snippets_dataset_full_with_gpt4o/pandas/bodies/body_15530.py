# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_clip.py
# Ensure that clipping method can handle NA values with out failing
# GH#40581

if nulls_fixture is pd.NaT:
    # constructor will raise, see
    #  test_constructor_mismatched_null_nullable_dtype
    exit()

ser = Series([nulls_fixture, 1.0, 3.0], dtype=any_numeric_ea_dtype)
s_clipped_upper = ser.clip(upper=2.0)
s_clipped_lower = ser.clip(lower=2.0)

expected_upper = Series([nulls_fixture, 1.0, 2.0], dtype=any_numeric_ea_dtype)
expected_lower = Series([nulls_fixture, 2.0, 3.0], dtype=any_numeric_ea_dtype)

tm.assert_series_equal(s_clipped_upper, expected_upper)
tm.assert_series_equal(s_clipped_lower, expected_lower)
