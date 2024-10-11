# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
alt = Timestamp(dt64)

assert ts == dt64
assert dt64 == ts
assert ts == alt
assert alt == ts

assert not ts != dt64
assert not dt64 != ts
assert not ts != alt
assert not alt != ts

assert not ts < dt64
assert not dt64 < ts
assert not ts < alt
assert not alt < ts

assert not ts > dt64
assert not dt64 > ts
assert not ts > alt
assert not alt > ts

assert ts >= dt64
assert dt64 >= ts
assert ts >= alt
assert alt >= ts

assert ts <= dt64
assert dt64 <= ts
assert ts <= alt
assert alt <= ts
