# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py

# Pass in scalar is disabled
scalar = Series(0.5)
assert not isinstance(scalar, float)

# Coercion
assert float(Series([1.0])) == 1.0
assert int(Series([1.0])) == 1
