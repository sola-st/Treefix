# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_constructors.py
msg = "dtype .*object.* cannot be converted to timedelta64"
with pytest.raises(ValueError, match=msg):
    TimedeltaArray._from_sequence([], dtype=object)
