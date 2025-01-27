# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_interval.py
interval = Interval(0, 1, closed=closed)
expected = Interval(1, 2, closed=closed)

result = interval + 1
assert result == expected

result = 1 + interval
assert result == expected

result = interval
result += 1
assert result == expected

msg = r"unsupported operand type\(s\) for \+"
with pytest.raises(TypeError, match=msg):
    interval + interval

with pytest.raises(TypeError, match=msg):
    interval + "foo"
