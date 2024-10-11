# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_stat_reductions.py

with pd.option_context("use_bottleneck", False):
    f = getattr(Series, name)

    # add some NaNs
    string_series_[5:15] = np.NaN

    # mean, idxmax, idxmin, min, and max are valid for dates
    if name not in ["max", "min", "mean", "median", "std"]:
        ds = Series(pd.date_range("1/1/2001", periods=10))
        msg = f"does not support reduction '{name}'"
        with pytest.raises(TypeError, match=msg):
            f(ds)

            # skipna or no
    assert pd.notna(f(string_series_))
    assert pd.isna(f(string_series_, skipna=False))

    # check the result is correct
    nona = string_series_.dropna()
    tm.assert_almost_equal(f(nona), alternate(nona.values))
    tm.assert_almost_equal(f(string_series_), alternate(nona.values))

    allna = string_series_ * np.nan

    if check_allna:
        assert np.isnan(f(allna))

    # dtype=object with None, it works!
    s = Series([1, 2, 3, None, 5])
    f(s)

    # GH#2888
    items = [0]
    items.extend(range(2**40, 2**40 + 1000))
    s = Series(items, dtype="int64")
    tm.assert_almost_equal(float(f(s)), float(alternate(s.values)))

    # check date range
    if check_objects:
        s = Series(pd.bdate_range("1/1/2000", periods=10))
        res = f(s)
        exp = alternate(s)
        assert res == exp

    # check on string data
    if name not in ["sum", "min", "max"]:
        with pytest.raises(TypeError, match=None):
            f(Series(list("abc")))

            # Invalid axis.
    msg = "No axis named 1 for object type Series"
    with pytest.raises(ValueError, match=msg):
        f(string_series_, axis=1)

    if "numeric_only" in inspect.getfullargspec(f).args:
        # only the index is string; dtype is float
        f(string_series_, numeric_only=True)
