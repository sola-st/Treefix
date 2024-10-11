# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# transforming functions

with np.errstate(all="ignore"):

    f_sqrt = np.sqrt(string_series)
    f_abs = np.abs(string_series)

    # ufunc
    result = string_series.apply(np.sqrt)
    expected = f_sqrt.copy()
    tm.assert_series_equal(result, expected)

    # list-like
    result = string_series.apply([np.sqrt])
    expected = f_sqrt.to_frame().copy()
    expected.columns = ["sqrt"]
    tm.assert_frame_equal(result, expected)

    result = string_series.apply(["sqrt"])
    tm.assert_frame_equal(result, expected)

    # multiple items in list
    # these are in the order as if we are applying both functions per
    # series and then concatting
    expected = concat([f_sqrt, f_abs], axis=1)
    expected.columns = ["sqrt", "absolute"]
    result = string_series.apply([np.sqrt, np.abs])
    tm.assert_frame_equal(result, expected)

    # dict, provide renaming
    expected = concat([f_sqrt, f_abs], axis=1)
    expected.columns = ["foo", "bar"]
    expected = expected.unstack().rename("series")

    result = string_series.apply({"foo": np.sqrt, "bar": np.abs})
    tm.assert_series_equal(result.reindex_like(expected), expected)
