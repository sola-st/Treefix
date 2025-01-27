# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
idx = PeriodIndex(
    [Period("2011-01", freq="M"), NaT, Period("2011-01", freq="M")]
)
exp = PeriodIndex(["2011-01", "NaT", "2011-01"], freq="M")
tm.assert_index_equal(idx, exp)

idx = PeriodIndex(
    np.array([Period("2011-01", freq="M"), NaT, Period("2011-01", freq="M")])
)
tm.assert_index_equal(idx, exp)

idx = PeriodIndex(
    [NaT, NaT, Period("2011-01", freq="M"), Period("2011-01", freq="M")]
)
exp = PeriodIndex(["NaT", "NaT", "2011-01", "2011-01"], freq="M")
tm.assert_index_equal(idx, exp)

idx = PeriodIndex(
    np.array(
        [NaT, NaT, Period("2011-01", freq="M"), Period("2011-01", freq="M")]
    )
)
tm.assert_index_equal(idx, exp)

idx = PeriodIndex([NaT, NaT, "2011-01", "2011-01"], freq="M")
tm.assert_index_equal(idx, exp)

with pytest.raises(ValueError, match="freq not specified"):
    PeriodIndex([NaT, NaT])

with pytest.raises(ValueError, match="freq not specified"):
    PeriodIndex(np.array([NaT, NaT]))

with pytest.raises(ValueError, match="freq not specified"):
    PeriodIndex(["NaT", "NaT"])

with pytest.raises(ValueError, match="freq not specified"):
    PeriodIndex(np.array(["NaT", "NaT"]))
