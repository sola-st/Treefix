# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_missing.py
# https://github.com/pandas-dev/pandas/issues/33594
with pd.option_context("mode.use_inf_as_na", True):
    cat = Categorical(values)
    result = cat.isna()
    tm.assert_numpy_array_equal(result, expected)

    result = Series(cat).isna()
    expected = Series(expected)
    tm.assert_series_equal(result, expected)

    result = DataFrame(cat).isna()
    expected = DataFrame(expected)
    tm.assert_frame_equal(result, expected)
