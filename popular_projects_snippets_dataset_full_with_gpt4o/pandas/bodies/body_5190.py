# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_constructors.py
exp, match = expectation
with pytest.raises(exp, match=match):
    _ = constructor(value, unit=unit)
