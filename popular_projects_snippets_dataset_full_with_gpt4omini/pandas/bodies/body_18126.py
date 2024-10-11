# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
rng = period_range("1/1/2000", freq="D", periods=5)
other = period_range("1/6/2000", freq="D", periods=5)
# TODO: parametrize over boxes for other?

rng = tm.box_expected(rng, box_with_array)
# An earlier implementation of PeriodIndex addition performed
# a set operation (union).  This has since been changed to
# raise a TypeError. See GH#14164 and GH#13077 for historical
# reference.
msg = r"unsupported operand type\(s\) for \+: .* and .*"
with pytest.raises(TypeError, match=msg):
    rng + other

with pytest.raises(TypeError, match=msg):
    rng += other
