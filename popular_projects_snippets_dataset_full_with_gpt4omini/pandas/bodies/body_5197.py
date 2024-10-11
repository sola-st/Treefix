# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# case where we are going neither to nor from nano
td = Timedelta(days=1).as_unit("ms")
assert td.days == 1
assert td.value == 86_400_000
assert td.components.days == 1
assert td._d == 1
assert td.total_seconds() == 86400

res = td.as_unit("us")
assert res.value == 86_400_000_000
assert res.components.days == 1
assert res.components.hours == 0
assert res._d == 1
assert res._h == 0
assert res.total_seconds() == 86400
