# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_interval.py
interval = Interval(1, 2, closed=closed)
expected = Interval(0, 1, closed=closed)

result = interval // 2
assert result == expected

result = interval
result //= 2
assert result == expected

msg = r"unsupported operand type\(s\) for //"
with pytest.raises(TypeError, match=msg):
    interval // interval

with pytest.raises(TypeError, match=msg):
    interval // "foo"
