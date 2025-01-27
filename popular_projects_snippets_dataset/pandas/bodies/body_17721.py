# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_ticks.py
assert_offset_equal(
    Milli(), Timestamp("2010-01-01"), Timestamp("2010-01-01 00:00:00.001")
)
assert_offset_equal(
    Milli(-1), Timestamp("2010-01-01 00:00:00.001"), Timestamp("2010-01-01")
)
