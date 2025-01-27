# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_asfreq.py
pi = PeriodIndex(["2001-01-01 00:00", "2001-01-02 02:00", "NaT"], freq="H")
exp = PeriodIndex(["2001-01-01 00:00", "2001-01-02 02:00", "NaT"], freq="25H")
for freq, how in zip(["1D1H", "1H1D"], ["S", "E"]):
    result = pi.asfreq(freq, how=how)
    tm.assert_index_equal(result, exp)
    assert result.freq == exp.freq

for freq in ["1D1H", "1H1D"]:
    pi = PeriodIndex(["2001-01-01 00:00", "2001-01-02 02:00", "NaT"], freq=freq)
    result = pi.asfreq("H")
    exp = PeriodIndex(["2001-01-02 00:00", "2001-01-03 02:00", "NaT"], freq="H")
    tm.assert_index_equal(result, exp)
    assert result.freq == exp.freq

    pi = PeriodIndex(["2001-01-01 00:00", "2001-01-02 02:00", "NaT"], freq=freq)
    result = pi.asfreq("H", how="S")
    exp = PeriodIndex(["2001-01-01 00:00", "2001-01-02 02:00", "NaT"], freq="H")
    tm.assert_index_equal(result, exp)
    assert result.freq == exp.freq
