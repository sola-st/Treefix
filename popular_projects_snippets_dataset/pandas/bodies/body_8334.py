# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_scalar_compat.py
# extra fields from DatetimeIndex like quarter and week
idx = tm.makeDateIndex(100)
expected = getattr(idx, field)[-1]

result = getattr(Timestamp(idx[-1]), field)
assert result == expected
