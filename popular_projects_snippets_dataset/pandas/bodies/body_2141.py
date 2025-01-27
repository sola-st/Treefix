# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# if we have a string, then we raise a ValueError
# and NOT an OutOfBoundsDatetime
msg = "non convertible value foo with the unit 's'"
with pytest.raises(ValueError, match=msg):
    to_datetime("foo", errors="raise", unit="s", cache=cache)
