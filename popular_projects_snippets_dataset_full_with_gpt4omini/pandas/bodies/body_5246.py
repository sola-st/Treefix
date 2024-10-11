# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
assert Timedelta(days=1).resolution_string == "D"
assert Timedelta(days=1, hours=6).resolution_string == "H"
assert Timedelta(days=1, minutes=6).resolution_string == "T"
assert Timedelta(days=1, seconds=6).resolution_string == "S"
assert Timedelta(days=1, milliseconds=6).resolution_string == "L"
assert Timedelta(days=1, microseconds=6).resolution_string == "U"
assert Timedelta(days=1, nanoseconds=6).resolution_string == "N"
