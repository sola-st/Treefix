# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_missing.py
# https://github.com/pandas-dev/pandas/issues/33594
# Using isna directly for Categorical will fail in general here
cat = Categorical(values)

with pd.option_context("mode.use_inf_as_na", True):
    result = isna(cat)
    tm.assert_numpy_array_equal(result, expected)

    result = isna(Series(cat))
    expected = Series(expected)
    tm.assert_series_equal(result, expected)

    result = isna(DataFrame(cat))
    expected = DataFrame(expected)
    tm.assert_frame_equal(result, expected)
