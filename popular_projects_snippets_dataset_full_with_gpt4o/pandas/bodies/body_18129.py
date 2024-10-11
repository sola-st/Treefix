# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
rng = period_range("1/1/2000", freq="D", periods=5)
other = period_range("1/6/2000", freq="H", periods=5)

rng = tm.box_expected(rng, box_with_array)
other = tm.box_expected(other, box_with_array2)
msg = r"Input has different freq=[HD] from PeriodArray\(freq=[DH]\)"
with pytest.raises(IncompatibleFrequency, match=msg):
    rng - other
