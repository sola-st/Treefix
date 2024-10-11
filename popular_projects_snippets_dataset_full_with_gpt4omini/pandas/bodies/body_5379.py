# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# GH#14440 & GH#15578
result = Timestamp("2016-10-17 12:00:00.0015").round("ms")
expected = Timestamp("2016-10-17 12:00:00.002000")
assert result == expected

result = Timestamp("2016-10-17 12:00:00.00149").round("ms")
expected = Timestamp("2016-10-17 12:00:00.001000")
assert result == expected

ts = Timestamp("2016-10-17 12:00:00.0015")
for freq in ["us", "ns"]:
    assert ts == ts.round(freq)

result = Timestamp("2016-10-17 12:00:00.001501031").round("10ns")
expected = Timestamp("2016-10-17 12:00:00.001501030")
assert result == expected
