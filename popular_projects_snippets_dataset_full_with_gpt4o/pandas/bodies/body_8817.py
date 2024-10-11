# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
# https://github.com/pandas-dev/pandas/issues/33655
values = pd.array(values, dtype=dtype)
with pd.option_context("mode.use_inf_as_na", True):
    result = values.isna()
    tm.assert_numpy_array_equal(result, expected)

    result = pd.Series(values).isna()
    expected = pd.Series(expected)
    tm.assert_series_equal(result, expected)

    result = pd.DataFrame(values).isna()
    expected = pd.DataFrame(expected)
    tm.assert_frame_equal(result, expected)
