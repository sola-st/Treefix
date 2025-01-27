# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#20829
t = Timedelta("1s")
msg = "not supported between instances of 'Timedelta' and '(int|str)'"
with pytest.raises(TypeError, match=msg):
    t >= val
with pytest.raises(TypeError, match=msg):
    t > val
with pytest.raises(TypeError, match=msg):
    t <= val
with pytest.raises(TypeError, match=msg):
    t < val
