# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
msg = "Units 'M', 'Y', and 'y' are no longer supported"
with pytest.raises(ValueError, match=msg):
    Timedelta(10, unit)

with pytest.raises(ValueError, match=msg):
    to_timedelta(10, unit)

with pytest.raises(ValueError, match=msg):
    to_timedelta([1, 2], unit)
