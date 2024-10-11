# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
rng = timedelta_range("1 days", "10 days", name="foo")
rng = tm.box_expected(rng, box_with_array)
msg = "argument must be an integer|cannot use operands with types dtype"
with pytest.raises(TypeError, match=msg):
    rng * two_hours
