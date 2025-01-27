# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
p = Period("Jan-2000")
assert "2000-01" in repr(p)

p = Period("2000-12-15")
assert "2000-12-15" in repr(p)
