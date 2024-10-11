# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
msg = "Units 'M', 'Y', and 'y' are no longer supported"
with pytest.raises(ValueError, match=msg):
    TimedeltaIndex([1, 3, 7], unit)
