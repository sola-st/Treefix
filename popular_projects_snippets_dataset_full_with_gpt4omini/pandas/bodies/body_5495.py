# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_comparisons.py
# see GH#1404
a = Timestamp("3/12/2012")
b = Timestamp("3/12/2012", tz=utc_fixture)

msg = "Cannot compare tz-naive and tz-aware timestamps"
assert not a == b
assert a != b
with pytest.raises(TypeError, match=msg):
    a < b
with pytest.raises(TypeError, match=msg):
    a <= b
with pytest.raises(TypeError, match=msg):
    a > b
with pytest.raises(TypeError, match=msg):
    a >= b

assert not b == a
assert b != a
with pytest.raises(TypeError, match=msg):
    b < a
with pytest.raises(TypeError, match=msg):
    b <= a
with pytest.raises(TypeError, match=msg):
    b > a
with pytest.raises(TypeError, match=msg):
    b >= a

assert not a == b.to_pydatetime()
assert not a.to_pydatetime() == b
