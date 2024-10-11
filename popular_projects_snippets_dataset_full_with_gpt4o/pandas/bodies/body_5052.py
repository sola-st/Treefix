# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_interval.py
interval = Interval(0, 1, closed=closed)
expected = Interval(0, 2, closed=closed)

result = interval * 2
assert result == expected

result = 2 * interval
assert result == expected

result = interval
result *= 2
assert result == expected

msg = r"unsupported operand type\(s\) for \*"
with pytest.raises(TypeError, match=msg):
    interval * interval

msg = r"can\'t multiply sequence by non-int"
with pytest.raises(TypeError, match=msg):
    interval * "foo"
