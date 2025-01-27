# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# normal ops are also tested in tseries/test_timedeltas.py
idx = TimedeltaIndex(["2H", "4H", "6H", "8H", "10H"], freq="2H", name="x")

for result in [idx * 2, np.multiply(idx, 2)]:
    assert isinstance(result, TimedeltaIndex)
    exp = TimedeltaIndex(["4H", "8H", "12H", "16H", "20H"], freq="4H", name="x")
    tm.assert_index_equal(result, exp)
    assert result.freq == "4H"

for result in [idx / 2, np.divide(idx, 2)]:
    assert isinstance(result, TimedeltaIndex)
    exp = TimedeltaIndex(["1H", "2H", "3H", "4H", "5H"], freq="H", name="x")
    tm.assert_index_equal(result, exp)
    assert result.freq == "H"

for result in [-idx, np.negative(idx)]:
    assert isinstance(result, TimedeltaIndex)
    exp = TimedeltaIndex(
        ["-2H", "-4H", "-6H", "-8H", "-10H"], freq="-2H", name="x"
    )
    tm.assert_index_equal(result, exp)
    assert result.freq == "-2H"

idx = TimedeltaIndex(["-2H", "-1H", "0H", "1H", "2H"], freq="H", name="x")
for result in [abs(idx), np.absolute(idx)]:
    assert isinstance(result, TimedeltaIndex)
    exp = TimedeltaIndex(["2H", "1H", "0H", "1H", "2H"], freq=None, name="x")
    tm.assert_index_equal(result, exp)
    assert result.freq is None
