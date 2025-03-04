# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_tz_convert.py
l0 = date_range("20140701", periods=5, freq="D")
l1 = date_range("20140701", periods=5, freq="D")

int_idx = Index(range(5))

if fn == "tz_convert":
    l0 = l0.tz_localize("UTC")
    l1 = l1.tz_localize("UTC")

for idx in [l0, l1]:

    l0_expected = getattr(idx, fn)("US/Pacific")
    l1_expected = getattr(idx, fn)("US/Pacific")

    df1 = DataFrame(np.ones(5), index=l0)
    df1 = getattr(df1, fn)("US/Pacific")
    tm.assert_index_equal(df1.index, l0_expected)

    # MultiIndex
    # GH7846
    df2 = DataFrame(np.ones(5), MultiIndex.from_arrays([l0, l1]))

    # freq is not preserved in MultiIndex construction
    l1_expected = l1_expected._with_freq(None)
    l0_expected = l0_expected._with_freq(None)
    l1 = l1._with_freq(None)
    l0 = l0._with_freq(None)

    df3 = getattr(df2, fn)("US/Pacific", level=0)
    assert not df3.index.levels[0].equals(l0)
    tm.assert_index_equal(df3.index.levels[0], l0_expected)
    tm.assert_index_equal(df3.index.levels[1], l1)
    assert not df3.index.levels[1].equals(l1_expected)

    df3 = getattr(df2, fn)("US/Pacific", level=1)
    tm.assert_index_equal(df3.index.levels[0], l0)
    assert not df3.index.levels[0].equals(l0_expected)
    tm.assert_index_equal(df3.index.levels[1], l1_expected)
    assert not df3.index.levels[1].equals(l1)

    df4 = DataFrame(np.ones(5), MultiIndex.from_arrays([int_idx, l0]))

    # TODO: untested
    df5 = getattr(df4, fn)("US/Pacific", level=1)  # noqa

    tm.assert_index_equal(df3.index.levels[0], l0)
    assert not df3.index.levels[0].equals(l0_expected)
    tm.assert_index_equal(df3.index.levels[1], l1_expected)
    assert not df3.index.levels[1].equals(l1)

# Bad Inputs

# Not DatetimeIndex / PeriodIndex
with pytest.raises(TypeError, match="DatetimeIndex"):
    df = DataFrame(index=int_idx)
    getattr(df, fn)("US/Pacific")

# Not DatetimeIndex / PeriodIndex
with pytest.raises(TypeError, match="DatetimeIndex"):
    df = DataFrame(np.ones(5), MultiIndex.from_arrays([int_idx, l0]))
    getattr(df, fn)("US/Pacific", level=0)

# Invalid level
with pytest.raises(ValueError, match="not valid"):
    df = DataFrame(index=l0)
    getattr(df, fn)("US/Pacific", level=1)
