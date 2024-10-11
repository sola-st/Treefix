# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# Shifting with PeriodIndex
ps = tm.makePeriodFrame()
ps = tm.get_obj(ps, frame_or_series)

shifted = ps.shift(1)
unshifted = shifted.shift(-1)
tm.assert_index_equal(shifted.index, ps.index)
tm.assert_index_equal(unshifted.index, ps.index)
if frame_or_series is DataFrame:
    tm.assert_numpy_array_equal(
        unshifted.iloc[:, 0].dropna().values, ps.iloc[:-1, 0].values
    )
else:
    tm.assert_numpy_array_equal(unshifted.dropna().values, ps.values[:-1])

shifted2 = ps.shift(1, "B")
shifted3 = ps.shift(1, offsets.BDay())
tm.assert_equal(shifted2, shifted3)
tm.assert_equal(ps, shifted2.shift(-1, "B"))

msg = "does not match PeriodIndex freq"
with pytest.raises(ValueError, match=msg):
    ps.shift(freq="D")

# legacy support
shifted4 = ps.shift(1, freq="B")
tm.assert_equal(shifted2, shifted4)

shifted5 = ps.shift(1, freq=offsets.BDay())
tm.assert_equal(shifted5, shifted4)
