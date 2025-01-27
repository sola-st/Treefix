# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# Separate Period objects for the same period
left = Period("2000-01", "M")
right = Period("2000-01", "M")

assert left == right
assert left >= right
assert left <= right
assert not left < right
assert not left > right
