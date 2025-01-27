# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_arithmetic.py
# no overflow expected

stamp = Timestamp("2000/1/1")
offset_no_overflow = to_offset("D") * 100

expected = Timestamp("2000/04/10")
assert stamp + offset_no_overflow == expected

assert offset_no_overflow + stamp == expected

expected = Timestamp("1999/09/23")
assert stamp - offset_no_overflow == expected
