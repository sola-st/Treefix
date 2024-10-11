# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
# GH #1264

years = np.arange(1990, 2010).repeat(4)[2:-2]
quarters = np.tile(np.arange(1, 5), 20)[2:-2]

index = PeriodIndex(year=years, quarter=quarters, freq="Q-DEC")
expected = period_range("1990Q3", "2009Q2", freq="Q-DEC")
tm.assert_index_equal(index, expected)

index2 = PeriodIndex(year=years, quarter=quarters, freq="2Q-DEC")
tm.assert_numpy_array_equal(index.asi8, index2.asi8)

index = PeriodIndex(year=years, quarter=quarters)
tm.assert_index_equal(index, expected)

years = [2007, 2007, 2007]
months = [1, 2]

msg = "Mismatched Period array lengths"
with pytest.raises(ValueError, match=msg):
    PeriodIndex(year=years, month=months, freq="M")
with pytest.raises(ValueError, match=msg):
    PeriodIndex(year=years, month=months, freq="2M")

years = [2007, 2007, 2007]
months = [1, 2, 3]
idx = PeriodIndex(year=years, month=months, freq="M")
exp = period_range("2007-01", periods=3, freq="M")
tm.assert_index_equal(idx, exp)
