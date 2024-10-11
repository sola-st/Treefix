# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# numpy gets this wrong because of silent overflow
other = Timedelta(days=106751, unit="ns")
assert other < td
assert td > other
assert not other == td
assert td != other
