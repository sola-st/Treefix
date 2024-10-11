# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_interval.py
msg = (
    "'<' not supported between instances of "
    "'pandas._libs.interval.Interval' and 'int'"
)
with pytest.raises(TypeError, match=msg):
    Interval(0, 1) < 2

assert Interval(0, 1) < Interval(1, 2)
assert Interval(0, 1) < Interval(0, 2)
assert Interval(0, 1) < Interval(0.5, 1.5)
assert Interval(0, 1) <= Interval(0, 1)
assert Interval(0, 1) > Interval(-1, 2)
assert Interval(0, 1) >= Interval(0, 1)
