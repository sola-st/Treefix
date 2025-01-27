# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
idx1 = PeriodIndex(["2011-01", "2011-02", "NaT", "2011-05"], freq=freq)

diff = PeriodIndex(["2011-02", "2011-01", "2011-04", "NaT"], freq="4M")
msg = rf"Invalid comparison between dtype=period\[{freq}\] and PeriodArray"
with pytest.raises(TypeError, match=msg):
    idx1 > diff

result = idx1 == diff
expected = np.array([False, False, False, False], dtype=bool)
tm.assert_numpy_array_equal(result, expected)
